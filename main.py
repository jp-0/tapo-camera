import typing as t

import click
import requests

from tapo_camera.cam import TapoCamera
from tapo_camera.provision_camera import (
    crude_user_choice,
    get_client_ips,
    guided_provisioning,
)
from tapo_camera.scan import generate_ip_range, scan_ips_for_cameras


@click.group()
def cli():
    pass


@cli.command(help="Provision a fresh camera so that it is minimally available for rtsp")
@click.option(
    "--camera-password",
    type=str,
    help="Password to set for controlling the camera (e.g. via this tool)",
    required=True,
)
@click.option(
    "--camera-alias",
    type=str,
    help="Set camera name (not for login, but helpful in device identification)",
    required=False,
)
@click.option(
    "--wifi-name",
    type=str,
    help="ESSID (name) of network to connect the camera to for regular operation",
    required=True,
)
@click.option(
    "--wifi-password",
    type=str,
    help="Password of network to connect the camera to for regular operation",
    required=True,
)
@click.option(
    "--third-user-name",
    type=str,
    help="Username to set for connecting to the camera after setup (rtsp streams)",
    required=True,
)
@click.option(
    "--third-user-password",
    type=str,
    help="Password to set for connecting to the camera after setup (rtsp streams)",
    required=True,
)
@click.option(
    "--timezone-id",
    type=str,
    help="Timezone identifier e.g. America/New_York",
    required=False,
)
@click.option(
    "--format-sd",
    type=bool,
    is_flag=True,
    help="Whether to re-format (wipe) the SD card inserted to the camera on setup",
)
def provision_camera(
    camera_password,
    camera_alias,
    wifi_name,
    wifi_password,
    third_user_name,
    third_user_password,
    timezone_id,
    format_sd,
):
    guided_provisioning(
        camera_password=camera_password,
        camera_alias=camera_alias,
        wifi_name=wifi_name,
        wifi_password=wifi_password,
        third_user_name=third_user_name,
        third_user_password=third_user_password,
        tz_region_name=timezone_id,
        format_sd=format_sd,
    )


@cli.command(
    help="Scan the /24 block of given interface for potential and confirmed cameras"
)
@click.option(
    "--camera-password",
    type=str,
    help="If known, use this password to confirm the device is a tapo camera and return the alias",
    required=False,
)
def find_cameras(camera_password: str):
    client_ips = get_client_ips()
    if len(client_ips) == 1:
        address = client_ips[0]
    else:
        address = crude_user_choice(client_ips, "Pick machine IP range to search on:")
    print(f"Scanning for cameras on interface {address}")
    potential_cameras = scan_ips_for_cameras(generate_ip_range(address))
    confirmed_cameras: t.Dict[str, TapoCamera] = {}

    if camera_password:
        for i in reversed(range(len(potential_cameras))):
            try:
                c = TapoCamera(potential_cameras[i], camera_password)
                confirmed_cameras[c.ip_address] = c
                potential_cameras.pop(i)
            except requests.exceptions.ConnectTimeout:
                pass

    if len(confirmed_cameras) > 0:
        print("Found confirmed cameras at:")
        for ip, cam in confirmed_cameras.items():
            print(f"{ip}: {cam.get_device_alias()}")
    if len(potential_cameras) > 0:
        print("Found potential cameras at:")
        for ip in potential_cameras:
            print(f"{ip}")

    return confirmed_cameras


if __name__ == "__main__":
    cli()
