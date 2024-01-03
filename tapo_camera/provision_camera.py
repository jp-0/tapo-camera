import socket
from datetime import datetime

import pytz
import requests

from tapo_camera.cam import ResponseError, TapoCamera
from tapo_camera.scan import (
    check_ip_address_format,
    generate_ip_range,
    scan_ips_for_cameras,
)


def guided_tz_selection():
    # TODO allow just to input the code directly
    tz_code = crude_user_choice(
        ["UTC"] + list(pytz.country_names.keys()), "Pick Timezone Code"
    )
    if tz_code == "UTC":
        tz = tz_code
    else:
        if len(pytz.country_timezones[tz_code]) == 1:
            tz = pytz.country_timezones[tz_code][0]
        else:
            tz = crude_user_choice(list(pytz.country_timezones[tz_code]), "Pick TZ")
    return tz


def crude_user_choice(acceptable_items: list, prompt: str):
    choice = None
    while choice not in acceptable_items:
        for i, ad in enumerate(acceptable_items):
            print(f"[{i}]: {ad}")
        choice = input(prompt + " (must select by index): ")
        try:
            choice = acceptable_items[int(choice)]
        except (IndexError, ValueError):
            pass
    return choice


def get_client_ips():
    # TODO move to scan.py
    client_addresses = flatten_list(list(socket.gethostbyname_ex(socket.gethostname())))
    return [
        a
        for a in client_addresses
        if a not in ("127.0.0.1") and check_ip_address_format(a)
    ]


def get_camera_connection_guided(password: str) -> TapoCamera:
    # Pick which IP of this machine to scan from for cameras
    client_address = crude_user_choice(
        get_client_ips(), "Select IP range to search for camera on:"
    )
    # Pick which remote IP is the camera
    tapo_ips = scan_ips_for_cameras(generate_ip_range(client_address))
    camera_ip = crude_user_choice(tapo_ips, "Select IP of tapo camera:")
    try:
        print("Attempting to connect to camera.")
        return TapoCamera(camera_ip, password)
    except requests.exceptions.ConnectTimeout:
        print(
            "Connection to camera timed out. Are you connected to the correct network?"
        )
        return None


def flatten_list(obj):
    if not isinstance(obj, list):
        return [obj]
    else:
        return [item for sublist in list(obj) for item in flatten_list(sublist)]


def guided_provisioning(
    *,
    camera_password: str,
    camera_alias: str,
    wifi_name: str,
    wifi_password: str,
    third_user_name: str,
    third_user_password: str,
    tz_region_name: str,
    format_sd: bool,
):
    # TODO error handling for failed responses / timeouts / etc

    tp = get_camera_connection_guided(camera_password)
    if tp is None:
        exit()

    attempt_no = 1
    attempt_max = 3
    ap = None
    while attempt_no <= attempt_max and ap is None:
        try:
            aps = tp.onboarding_get_access_points()
        except ResponseError:
            print("Camera has already been set up. Reset camera using button on device")
            exit()
        try:
            ap = [ap for ap in aps if ap["ssid"] == wifi_name][0]
        except IndexError:
            print(
                f"Camera could not find network ({wifi_name}), "
                f"retrying (attempt {attempt_no}/{attempt_max})"
            )
    if ap is None:
        print(f"Camera could not find network ({wifi_name})")
        exit()

    # Set camera configuration items prior to connecting it to the access point
    # Follows the traffic dump of the application
    ap["password"] = wifi_password
    tp.set_language("EN")
    tp.set_admin_password(camera_password)
    tp.set_media_encrypt_on()
    if tz_region_name is None:
        # Determine and set timezone (TODO doesn't currently account for DST)
        tz_id = guided_tz_selection()
        offset = datetime.now(pytz.timezone(tz_id)).strftime("%z")
        tz_offset = (
            f"UTC{'-' if offset[0] not in ('-', '+') else ''}{offset[:-2]}:{offset[-2:]}"
        )
        tp.set_timezone(tz_offset, tz_id)  # will use NTP
    # Remaining setup and connect
    tp.set_default_recording_plan()()
    tp.onboarding_set_access_point(**ap)

    # Re-establish connection with camera and execute the 'initialisation commands'
    # Follows the traffic dump of the application
    input("Once re-connected to your network press enter")
    tp = get_camera_connection_guided(camera_password)
    while tp is None or type(tp) == ResponseError:
        input("Once re-connected to your network press enter to try again")
        input("Or maybe camera failed to connect to the AP")
        tp = get_camera_connection_guided(camera_password)
    if format_sd:
        tp.format_sd_card()
    tp.get_sdcard_info()  # This is not necessary but is part of the tapo app process so have kept it
    if camera_alias:
        tp.set_device_alias(camera_alias)
    tp.set_third_user_first(third_user_name, third_user_password)

    rtsp_url = (
        f"rtsp://{third_user_name}:{third_user_password}@{tp.ip_address}:544/stream1"
    )
    print(f"Access camera stream at:\n{rtsp_url}")
