import hashlib
from base64 import b64decode, b64encode
from datetime import datetime

import pytz
import requests
import urllib3
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from Crypto.PublicKey import RSA

# FIXME change this so it is per-request and inside the _request method of TapoCamera
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# TODO consider how to return the error codes appropriately
# TODO figure which that use multipleRequest also work as single requests

PUBLIC_KEY = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4D6i0oD/Ga5qb//RfSe8MrPVIrMIGecCxkcGWGj9kxxk74qQNq8XUuXoy2PczQ30BpiRHrlkbtBEPeWLpq85tfubTUjhBz1NPNvWrC88uaYVGvzNpgzZOqDC35961uPTuvdUa8vztcUQjEZy16WbmetRjURFIiWJgFCmemyYVbQIDAQAB"


class ResponseError(Exception):
    pass


class RequestSuccess:
    pass


class RequestFailure:
    pass


class TapoCamera:
    def __init__(self, ip_address, password):
        self.ip_address = ip_address
        self.password = password
        self.url = f"https://{self.ip_address}/"
        self.stok = self.get_stok()
        self.cipher = Cipher_PKCS1_v1_5.new(RSA.importKey(b64decode(PUBLIC_KEY)))

    def _request(self, post_req: dict, authenticated: bool = False):
        # TODO consider how to get a fresh 'stok' login if request fails (and when to)
        if authenticated:
            url = self.url + f"stok={self.stok}/ds"
        else:
            url = self.url
        # the camera's supported encryption settings are low, so do not verify the certificate in POST request
        response = requests.post(url, json=post_req, verify=False).json()
        # TODO consider how the multipleRequest items should be tested against the error_code, as there is a general one and one per sub function requested. However, only ever doing a single request in each multipleRequest in this API
        if response["error_code"] != 0:
            raise ResponseError(response)
        elif post_req.get("method") == "setLanguage":
            return response
        else:
            return response["result"]

    def _single_request(self, method: str, params: dict, authenticated: bool = False):
        post_req = {"method": method, "params": params}
        return self._request(post_req, authenticated=authenticated)

    def _multi_request(self, method: str, params: dict, authenticated: bool = False):
        post_req = {
            "method": "multipleRequest",
            "params": {"requests": [{"method": method, "params": params}]},
        }
        return self._request(post_req, authenticated=authenticated)

    def request_manual(self, post_req, authenticated=False):
        # post_req e.g.: {'method': 'multipleRequest', 'params': {'requests': [{'method': 'getVideoCapability', 'params': {"video_capability": {"name": ["main", 'minor']}}}]}}
        # authenticated: undertake authentication of 'stok' for this operation
        return self._request(post_req, authenticated)

    def get_stok(self):
        result = self._single_request(
            "login",
            {
                "hashed": True,
                "password": self._get_md5(
                    self.password
                ),  # MD5 HASH of the password, with ALL Capital Letters
                "username": "admin",
            },
            authenticated=False,
        )
        return result["stok"]

    def reboot(self):
        result = self._multi_request("rebootDevice", {"system": {"reboot": {}}}, True)
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def get_video_capabilities(self):
        # TODO there are a lot of settings here, probably there are equivalent ways to set them
        result = self._multi_request(
            "getVideoCapability",
            {"video_capability": {"name": ["main", "minor"]}},
            True,
        )
        return result["responses"][0]["result"]["video_capability"]

    def get_available_resolutions_main(self):
        # the primary stream
        result = self.get_video_capabilities()
        return result["main"]["resolutions"]

    def get_available_resolutions_minor(self):
        # the second stream
        result = self.get_video_capabilities()
        return result["minor"]["resolutions"]

    def set_resolution_main(self, resolution: str) -> str:
        result = self._multi_request(
            "setResolution",
            {
                "video": {
                    "set_resolution": {"resolution": resolution, "secname": "main"}
                }
            },
            True,
        )
        response_code = result["responses"][0]["error_code"]
        # error_code of -61912 means that the camera is already set to this resolution
        if response_code in (0, -61912):
            return resolution
        raise ResponseError()

    # def set_resolution_minor(self, resolution: str) -> str:
    #     result = self._multi_request('setResolution', {"video": {"set_resolution": {"resolution": resolution, "secname": "minor"}}}, True)
    #     response_code = result['responses'][0]['error_code']
    #     # error_code of -61912 means that the camera is already set to this resolution
    #     if response_code in (0, -61912):
    #         return resolution
    #     raise ResponseError()

    def get_video_qualities(self):
        result = self._multi_request(
            "getVideoQualities", {"video": {"name": ["main", "minor"]}}, True
        )
        return result["responses"][0]["result"]

    def get_current_resolution(self):
        # TODO allow to return minor resolution also
        result = self.get_video_qualities()
        return result["video"]["main"]["resolution"]

    def get_app_data(self):
        result = self._multi_request(
            "getAppComponentList",
            {"app_component": {"name": "app_component_list"}},
            True,
        )
        return result["responses"][0]["result"]["app_component"]

    def get_day_night_config(self):
        # TODO is there an equivalent set method in the API?
        result = self._multi_request(
            "getDayNightModeConfig", {"image": {"name": "common"}}, True
        )
        return result["responses"][0]["result"]

    def set_privacy_mode(self, on: bool):
        enabled = "on" if on else "off"
        result = self._multi_request(
            "setLensMaskConfig",
            {"lens_mask": {"lens_mask_info": {"enabled": enabled}}},
            True,
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_day_night(self, mode):
        if mode == "day":
            inf_type = "off"
        elif mode == "night":
            inf_type = "on"
        elif mode == "auto":
            inf_type = "auto"
        else:
            raise ValueError("day_night mode must be one of: day, night, or auto")
        result = self._multi_request(
            "setDayNightModeConfig", {"image": {"common": {"inf_type": inf_type}}}, True
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def format_sd_card(self):
        result = self._multi_request(
            "formatSdCard", {"harddisk_manage": {"format_hd": "1"}}, True
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_device_alias(self, name: str):
        result = self._multi_request(
            "setDeviceAlias", {"system": {"sys": {"dev_alias": name}}}, True
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def get_device_info(self):
        result = self._multi_request(
            "getDeviceInfo", {"device_info": {"name": ["basic_info"]}}, True
        )
        return result["responses"][0]["result"]["device_info"]

    def get_last_alarm_info(self):
        result = self._multi_request(
            "getLastAlarmInfo", {"system": {"name": ["last_alarm_info"]}}, True
        )
        return result["responses"][0]["result"]['system']

    def get_device_alias(self):
        return self.get_device_info()["basic_info"]["device_alias"]

    def get_audio_config(self):
        result = self._multi_request(
            "getAudioConfig",
            {"audio_config": {"name": ["speaker", "microphone", "record_audio"]}},
            True,
        )
        return result["responses"][0]["result"]["audio_config"]

    def get_lens_mask_config(self):
        result = self._multi_request(
            "getLensMaskConfig", {"lens_mask": {"name": ["lens_mask_info"]}}, True
        )
        return result["responses"][0]["result"]["lens_mask"]

    def get_sdcard_info(self):
        result = self._multi_request(
            "getSdCardStatus", {"harddisk_manage": {"table": ["hd_info"]}}, True
        )
        return result["responses"][0]["result"]

    def get_recording_circular_setting(self):
        # whether the recording will loop and overwrite
        # TODO is there a way to set this?
        result = self._multi_request(
            "getCircularRecordingConfig",
            {"harddisk_manage": {"name": ["harddisk"]}},
            True,
        )
        return result["responses"][0]["result"]

    def get_alert_config(self):
        # TODO multiple channels
        result = self._multi_request(
            "getAlertConfig", {"msg_alarm": {"name": ["chn1_msg_alarm_info"]}}, True
        )
        return result["responses"][0]["result"]

    def invert_video(self):
        # TODO put functions to set it in each direction explicitly instead of just flipping
        if self.get_video_orientation() == "off":
            flip_type = "center"
        else:
            flip_type = "off"
        result = self._multi_request(
            "setRotationStatus", {"image": {"switch": {"flip_type": flip_type}}}, True
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def get_video_settings(self):
        result = self._multi_request("getLdc", {"image": {"name": "switch"}}, True)
        return result["responses"][0]["result"]

    def get_video_orientation(self):
        result = self.get_video_settings()["image"]["switch"]["flip_type"]
        return result

    def set_led_off(self):
        # TODO how to check status
        result = self._multi_request(
            "setLedStatus", {"led": {"config": {"enabled": "off"}}}, True
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_led_on(self):
        result = self._multi_request(
            "setLedStatus", {"led": {"config": {"enabled": "on"}}}, True
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def get_clock_status(self):
        result = self._multi_request(
            "getClockStatus", {"system": {"name": "clock_status"}}, True
        )
        return result["responses"][0]["result"]

    def get_dst_rule(self):
        result = self._multi_request("getDstRule", {"system": {"name": "dst"}}, True)
        return result["responses"][0]["result"]

    def get_timezone(self):
        result = self._multi_request("getTimezone", {"system": {"name": "basic"}}, True)
        return result["responses"][0]["result"]

    def set_timezone(self, zone_name: str, utc_offset: str = None):
        # zone_name: America/New_York
        # utc_offset: UTC-07:00
        if not utc_offset:
            offset = datetime.now(pytz.timezone(zone_name)).strftime("%z")
            utc_offset = f"UTC{'-' if offset[0] not in ('-', '+') else ''}{offset[:-2]}:{offset[-2:]}"
        # timing_mode can be "ntp" or "manual", but unclear how to set the time if in manual mode
        # TODO appears the time can only be set manually via ONVIF
        template = {
            "system": {
                "basic": {
                    "timing_mode": "ntp",
                    "timezone": utc_offset,
                    "zone_id": zone_name,
                }
            }
        }
        result = self._multi_request("setTimezone", template, True)
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_media_encrypt_on(self):
        # TODO what media does this refer to? is it the stream or the storage?
        result = self._multi_request(
            "setMediaEncrypt", {"cet": {"media_encrypt": {"enabled": "on"}}}, True
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_media_encrypt_off(self):
        # TODO what media does this refer to? is it the stream or the storage?
        result = self._multi_request(
            "setMediaEncrypt", {"cet": {"media_encrypt": {"enabled": "off"}}}, True
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def get_osd(self):
        result = self._multi_request(
            "getOsd",
            {
                "OSD": {
                    "name": ["logo", "date", "week", "font"],
                    "table": ["label_info"],
                }
            },
            True,
        )
        return result["responses"][0]["result"]

    def set_osd_logo_disable(self):
        # TODO create a osd_text_toggle
        # TODO create enable/disable for each of the 'logo', 'date', 'week' options
        result = self._multi_request(
            "setOsd",
            {"OSD": {"logo": {"enabled": "off", "x_coor": "0", "y_coor": "9150"}}},
            True,
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_osd_logo_enable(self):
        result = self._multi_request(
            "setOsd",
            {"OSD": {"logo": {"enabled": "on", "x_coor": "0", "y_coor": "9150"}}},
            True,
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_osd_text(self, text: str, show_date: bool = True, show_week: bool = False):
        # TODO make fuctions to turn on and off the date, week, and text
        # TODO what are the colour options available for the font?
        # TODO able to move the locations around
        # TODO check if need to set all the 'date', 'week', 'font', 'label_info_1' at once or can do indivisually
        template = {
            "OSD": {
                "date": {
                    "enabled": "on" if show_date else "off",
                    "x_coor": "0",
                    "y_coor": "0",
                },
                "week": {
                    "enabled": "on" if show_week else "off",
                    "x_coor": "0",
                    "y_coor": "0",
                },
                "font": {
                    "color": "white",
                    "color_type": "auto",
                    "display": "ntnb",
                    "size": "auto",
                },
                "label_info_1": {
                    "enabled": "on",
                    "text": text,
                    "x_coor": "0",
                    "y_coor": "500",
                },
            }
        }
        result = self._multi_request("setOsd", template, True)
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_diagnose_mode_on(self):
        # turn diagnostics logging to SDcard on
        result = self._multi_request(
            "setDiagnoseMode", {"system": {"sys": {"diagnose_mode": "on"}}}, True
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_diagnose_mode_off(self):
        # turn diagnostics logging to SDcard off
        # TODO (should call checkDiagnoseStatus after, if it returns "stopped" then could be no SD card inserted)
        result = self._multi_request(
            "setDiagnoseMode", {"system": {"sys": {"diagnose_mode": "off"}}}, True
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def get_diagnose_mode(self):
        # check whether diagnostics logging to SDcard is on or off
        result = self._multi_request(
            "getDiagnoseMode", {"system": {"name": "sys"}}, True
        )
        return result["responses"][0]["result"]

    def get_diagnose_status(self):
        result = self._multi_request(
            "checkDiagnoseStatus", {"system": {"check_diagnose_status": ""}}, True
        )
        return result["responses"][0]["result"]

    def get_light_frequency_info(self):
        result = self._multi_request(
            "getLightFrequencyInfo", {"image": {"name": "common"}}, True
        )
        return result["responses"][0]["result"]

    def set_admin_password(self, password):
        # raise NotImplementedError()
        # FIXME not quite working
        template = {
            "user_management": {
                "change_admin_password": {
                    "secname": "root",
                    "passwd": self._get_md5(password),
                    "old_passwd": self.password,
                    "ciphertext": self._get_rsa(password),
                    "username": "admin",
                }
            }
        }
        result = self._multi_request(
            "changeAdminPassword", template, authenticated=True
        )
        if result["responses"][0]["error_code"] == 0:
            self.password = password
            return RequestSuccess()
        else:
            return RequestFailure()

    def get_third_account(self):
        result = self._multi_request(
            "getThirdAccount", {"user_management": {"name": ["third_account"]}}, True
        )
        return result["responses"][0]["result"]

    def get_user_id(self):
        # unclear what the information this returns means
        result = self._multi_request(
            "getUserID", {"system": {"get_user_id": "null"}}, True
        )
        return result["responses"][0]["result"]

    def get_network_connection_type(self):
        result = self._multi_request(
            "getConnectionType", {"network": {"get_connection_type": ["null"]}}, True
        )
        return result["responses"][0]["result"]

    def get_ip(self):
        result = self._multi_request(
            "getDeviceIpAddress", {"network": {"name": ["wan"]}}, True
        )
        return result["responses"][0]["result"]

    def onboarding_get_access_points(self):
        # search for wifi
        result = self._single_request(
            "scanApList", {"onboarding": {"scan": {}}}, authenticated=False
        )
        # TODO error code of -40101 MAY mean the device is no longer in onboarding mode
        return result["onboarding"]["scan"]["ap_list"]

    def onboarding_set_access_point(
        self,
        ssid: str,
        password: str,
        bssid: str,
        auth: int,
        encryption: int,
        rssi: int,
    ):
        # connect to wifi
        encrypted_password = self._get_rsa(password)

        result = self._single_request(
            "connectAp",
            {
                "onboarding": {
                    "connect": {
                        "auth": auth,
                        "bssid": bssid,
                        "encryption": encryption,
                        "password": encrypted_password,
                        "rssi": rssi,
                        "ssid": ssid,
                    }
                }
            },
            False,
        )
        return result["onboarding"]

    def onboarding_get_connection_status(self):
        result = self._single_request(
            "getConnectStatus", {"onboarding": {"get_connect_status": {}}}, False
        )
        return result["responses"][0]["result"]

    def set_language(self, language: str):
        # TODO how to get list of supported languages?
        result = self._single_request("setLanguage", {"language": language}, False)
        return RequestSuccess() if result["error_code"] == 0 else RequestFailure()

    def set_default_recording_plan(self):
        # TODO change to use `set_recording_plan` once it is implemented
        result = self._multi_request(
            "setRecordPlan",
            {
                "record_plan": {
                    "chn1_channel": {  # TODO there are multiple channels
                        "enabled": "on",  # TODO a way to disable and enable existing plans
                        "friday": '["0000-2400:2"]',
                        "monday": '["0000-2400:2"]',
                        "saturday": '["0000-2400:2"]',
                        "sunday": '["0000-2400:2"]',
                        "thursday": '["0000-2400:2"]',
                        "tuesday": '["0000-2400:2"]',
                        "wednesday": '["0000-2400:2"]',
                    }
                }
            },
            True,
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_recording_plan(self):
        raise NotImplementedError
        # TODO allow to set different plans
        result = self._multi_request(
            "setRecordPlan",
            {
                "record_plan": {
                    "chn1_channel": {
                        "enabled": "on",
                        "friday": '["0000-2400:2"]',
                        "monday": '["0000-2400:2"]',
                        "saturday": '["0000-2400:2"]',
                        "sunday": '["0000-2400:2"]',
                        "thursday": '["0000-2400:2"]',
                        "tuesday": '["0000-2400:2"]',
                        "wednesday": '["0000-2400:2"]',
                    }
                }
            },
            True,
        )
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def get_detection_config(self):
        result = self._multi_request(
            "getDetectionConfig", {"motion_detection": {"name": ["motion_det"], "table": ["region_info"]}}, True
        )
        return result["responses"][0]["result"]

    def set_motion_detection_sensitivity(self, setting: str):
        # TODO improve approach rather 'special strings'
        if setting == 'high':
            level = 80
        elif setting == 'medium':
            level = 50
        elif setting == 'low':
            level = 20
        else:
            raise ValueError('Error setting motion sensitivity, unknown level')
        result = self._multi_request(
            "setDetectionConfig", {"motion_detection": {"motion_det": {"digital_sensitivity": str(level)}}}, True
        )
        return result["responses"][0]["result"]

    def set_motion_detection(self, on: bool):
        enabled = "on" if on else "off"
        result = self._multi_request(
            "setDetectionConfig", {"motion_detection": {"motion_det": {"enabled": enabled}}}, True
        )
        return result["responses"][0]["result"]

    def get_msg_push_config(self):
        result = self._multi_request(
            "getMsgPushConfig", {"msg_push": {"name": ["chn1_msg_push_info"]}}, True
        )
        return result["responses"][0]["result"]

    def get_person_detection_config(self):
        result = self._multi_request(
            "getPersonDetectionConfig", {"people_detection": {"name": ["detection"]}}, True
        )
        return result["responses"][0]["result"]

    def _get_md5(self, text):
        return hashlib.md5(text.encode()).hexdigest().upper()

    def _get_rsa(self, text):
        return b64encode(self.cipher.encrypt(text.encode())).decode()

    def set_third_user(
        self, current_username, current_password, new_username, new_password
    ):
        new_third_account_password_md5 = self._get_md5(new_password)
        current_third_account_password_md5 = self._get_md5(current_password)
        new_third_account_password_rsa = self._get_rsa(new_password)
        current_third_account_password_rsa = self._get_rsa(current_password)

        ## after changeThirdAccount is done the first time, the app does not allow for the username to be changed unless first do a verifyThirdAccount and then a changeThirdAccount
        post_req = {
            "method": "multipleRequest",
            "params": {
                "requests": [
                    {
                        "method": "verifyThirdAccount",
                        "params": {
                            "user_management": {
                                "verify_third_account": {
                                    "secname": "third_account",
                                    "passwd": current_third_account_password_md5,
                                    "old_passwd": "",
                                    "ciphertext": current_third_account_password_rsa,
                                    "username": current_username,
                                }
                            }
                        },
                    }
                ]
            },
        }
        result = self._request(post_req, authenticated=True)
        if result["responses"][0]["error_code"] != 0:
            # TODO pass this message in the failure error message
            # 'Failed to change Third Account: Is the current username and password correct?'
            raise RequestFailure()
        # change both username and password we're authenticated
        post_req = {
            "method": "multipleRequest",
            "params": {
                "requests": [
                    {
                        "method": "changeThirdAccount",
                        "params": {
                            "user_management": {
                                "change_third_account": {
                                    "secname": "third_account",
                                    "passwd": new_third_account_password_md5,
                                    "old_passwd": "",
                                    "ciphertext": new_third_account_password_rsa,
                                    "username": new_username,
                                }
                            }
                        },
                    }
                ]
            },
        }

        result = self._request(post_req, authenticated=True)
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )

    def set_third_user_first(self, new_username, new_password):
        new_third_account_password_md5 = self._get_md5(new_password)
        new_third_account_password_rsa = self._get_rsa(new_password)

        post_req = {
            "method": "multipleRequest",
            "params": {
                "requests": [
                    {
                        "method": "changeThirdAccount",
                        "params": {
                            "user_management": {
                                "change_third_account": {
                                    "secname": "third_account",
                                    "passwd": new_third_account_password_md5,
                                    "old_passwd": "",
                                    "ciphertext": new_third_account_password_rsa,
                                    "username": new_username,
                                }
                            }
                        },
                    }
                ]
            },
        }

        result = self._request(post_req, authenticated=True)
        return (
            RequestSuccess()
            if result["responses"][0]["error_code"] == 0
            else RequestFailure()
        )
