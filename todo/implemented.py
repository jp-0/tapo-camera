# reboot camera
{
    "method": "multipleRequest",
    "params": {
        "requests": [{"method": "rebootDevice", "params": {"system": {"reboot": {}}}}]
    },
}
# get day/night configuration information
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {"method": "getDayNightModeConfig", "params": {"image": {"name": "common"}}}
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getDayNightModeConfig",
                "result": {
                    "image": {
                        "common": {
                            ".name": "common",
                            ".type": "para",
                            "luma": "50",
                            "contrast": "50",
                            "chroma": "50",
                            "saturation": "50",
                            "sharpness": "50",
                            "exp_type": "auto",
                            "shutter": "1\/25",
                            "focus_type": "semi_auto",
                            "focus_limited": "600",
                            "exp_gain": "0",
                            "inf_type": "auto",
                            "inf_start_time": "64800",
                            "inf_end_time": "21600",
                            "inf_sensitivity": "4",
                            "inf_delay": "5",
                            "wide_dynamic": "off",
                            "light_freq_mode": "auto",
                            "wd_gain": "50",
                            "wb_type": "auto",
                            "wb_R_gain": "50",
                            "wb_G_gain": "50",
                            "wb_B_gain": "50",
                            "lock_red_gain": "0",
                            "lock_gr_gain": "0",
                            "lock_gb_gain": "0",
                            "lock_blue_gain": "0",
                            "lock_red_colton": "0",
                            "lock_green_colton": "0",
                            "lock_blue_colton": "0",
                            "lock_source": "local",
                            "area_compensation": "default",
                            "smartir": "off",
                            "smartir_level": "100",
                            "high_light_compensation": "off",
                            "dehaze": "off",
                        }
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}
# set day mode
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setDayNightModeConfig",
                "params": {"image": {"common": {"inf_type": "off"}}},
            }
        ]
    },
}
# set night mode
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setDayNightModeConfig",
                "params": {"image": {"common": {"inf_type": "on"}}},
            }
        ]
    },
}
# set auto mode (auto doesn't flip back to the 'best' setting of day/night very well, so may have to flip it manually)
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setDayNightModeConfig",
                "params": {"image": {"common": {"inf_type": "auto"}}},
            }
        ]
    },
}


# username: user_name, password: bobbob
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "changeThirdAccount",
                "params": {
                    "user_management": {
                        "change_third_account": {
                            "secname": "third_account",
                            "passwd": "E8557D12F6551B2DDD26BBDD0395465C",
                            "old_passwd": "",
                            "ciphertext": "G/fkQ7iYMpKJL100vAqFmEXFzLpMSSzNNtpnSo6lW8n4/BA0whA5PNJL8NoQi6nCZV/BCdVhKSRvLdhlfihS5b43bZLizqsbRl6eHfq253u5afQ5jc5LdJeWQauHTF8ogVFFnHVjSdLo/iB7/pbYt1JyNlnX7uo4H9sVw2IfRWI=",
                            "username": "user_name",
                        }
                    }
                },
            }
        ]
    },
}
# -50925 response means incorrect password
## after changeThirdAccount is done the first time, the app does not allow for the username to be changed unless first do a verifyThirdAccount and then a changeThirdAccount
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "verifyThirdAccount",
                "params": {
                    "user_management": {
                        "verify_third_account": {
                            "secname": "third_account",
                            "passwd": "E8557D12F6551B2DDD26BBDD0395465C",
                            "old_passwd": "",
                            "ciphertext": "l/RUSY7BpvSfovwZHG4o+FCFYoM1anStXFCd5Vcvpf321wgTlhb+TcGAeX1NgrRuiBObnZDWOmFuOGGhKBUGgQo/hHNMmqo28WB5FhJSL2Z8+wLLQ9hXJFMHaZUI6pAzXJEqbPScNnC00crkHIkTczNlvj0fmfqHqXWeU7qb8o0=",
                            "username": "user_name",
                        }
                    }
                },
            }
        ]
    },
}
# change both username and password to now be: username: user_name2, password: bobbob2
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "changeThirdAccount",
                "params": {
                    "user_management": {
                        "change_third_account": {
                            "secname": "third_account",
                            "passwd": "9B811C73586E67EA750748B89A2C13BF",
                            "old_passwd": "",
                            "ciphertext": "gQbq02nxCST4fwzVvh66vlBKgAb2o6HSFEI1V/piqoDlaZZHjbs5xzH/0L+Zi6na5VQkrorvPoXWcChapUPKaLkcZ3oqO5NycBqzRiSSPQPYyUexm0FJPNmPWutgEs9v/4Rhos2frOsIHUr+kDZmAj3+D4XEil7gemNO81amnUA=",
                            "username": "user_name2",
                        }
                    }
                },
            }
        ]
    },
}

## privacy mode
### turn on
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setLensMaskConfig",
                "params": {"lens_mask": {"lens_mask_info": {"enabled": "on"}}},
            }
        ]
    },
}
### turn off
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setLensMaskConfig",
                "params": {"lens_mask": {"lens_mask_info": {"enabled": "off"}}},
            }
        ]
    },
}

# set the camera name
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setDeviceAlias",
                "params": {"system": {"sys": {"dev_alias": "mycamera2"}}},
            }
        ]
    },
}

# audio information
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getAudioConfig",
                "params": {"audio_config": {"name": ["speaker", "microphone"]}},
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getAudioConfig",
                "result": {
                    "audio_config": {
                        "speaker": {
                            ".name": "speaker",
                            ".type": "audio_config",
                            "volume": "100",
                        },
                        "microphone": {
                            ".name": "microphone",
                            ".type": "audio_config",
                            "sampling_rate": "8",
                            "channels": "1",
                            "encode_type": "G711alaw",
                            "volume": "100",
                            "mute": "off",
                            "noise_cancelling": "on",
                        },
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}
# POST /stok=3e4f89ff85c237e86e849d7f85900079/ds
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getLensMaskConfig",
                "params": {"lens_mask": {"name": ["lens_mask_info"]}},
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getLensMaskConfig",
                "result": {
                    "lens_mask": {
                        "lens_mask_info": {
                            ".name": "lens_mask_info",
                            ".type": "lens_mask_info",
                            "enabled": "off",
                        }
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}

# POST /stok=3e4f89ff85c237e86e849d7f85900079/ds
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getSdCardStatus",
                "params": {"harddisk_manage": {"table": ["hd_info"]}},
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getSdCardStatus",
                "result": {
                    "harddisk_manage": {
                        "hd_info": [
                            {
                                "hd_info_1": {
                                    "disk_name": "1",
                                    "rw_attr": "r",
                                    "status": "offline",
                                    "detect_status": "offline",
                                    "write_protect": "0",
                                    "percent": "0",
                                    "type": "local",
                                    "record_duration": "0",
                                    "record_free_duration": "0",
                                    "record_start_time": "0",
                                    "loop_record_status": "0",
                                    "total_space": "0B",
                                    "free_space": "0B",
                                    "video_total_space": "0B",
                                    "video_free_space": "0B",
                                    "picture_total_space": "0B",
                                    "picture_free_space": "0B",
                                    "msg_push_total_space": "0B",
                                    "msg_push_free_space": "0B",
                                }
                            }
                        ]
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}

# POST /stok=3e4f89ff85c237e86e849d7f85900079/ds
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getAlertConfig",
                "params": {"msg_alarm": {"name": ["chn1_msg_alarm_info"]}},
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getAlertConfig",
                "result": {
                    "msg_alarm": {
                        "chn1_msg_alarm_info": {
                            ".name": "chn1_msg_alarm_info",
                            ".type": "info",
                            "enabled": "off",
                            "alarm_type": "0",
                            "light_type": "1",
                            "alarm_mode": ["sound", "light"],
                            "sound_alarm_enabled": "off",
                            "light_alarm_enabled": "off",
                        }
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}

# check or set the video quality
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {"method": "getVideoQualities", "params": {"video": {"name": ["main"]}}}
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getVideoQualities",
                "result": {
                    "video": {
                        "main": {
                            ".name": "main",
                            ".type": "stream",
                            "stream_type": "general",
                            "resolution": "1920*1080",
                            "bitrate_type": "vbr",
                            "frame_rate": "65551",
                            "quality": "3",
                            "bitrate": "2048",
                            "encode_type": "H264",
                            "name": "VideoEncoder_1",
                        }
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}

# set resolution
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setResolution",
                "params": {
                    "video": {
                        "set_resolution": {"resolution": "2304*1296", "secname": "main"}
                    }
                },
            }
        ]
    },
}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setResolution",
                "params": {
                    "video": {
                        "set_resolution": {"resolution": "1920*1080", "secname": "main"}
                    }
                },
            }
        ]
    },
}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setResolution",
                "params": {
                    "video": {
                        "set_resolution": {"resolution": "1280*720", "secname": "main"}
                    }
                },
            }
        ]
    },
}
# invert the camera view
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setRotationStatus",
                "params": {"image": {"switch": {"flip_type": "center"}}},
            }
        ]
    },
}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setRotationStatus",
                "params": {"image": {"switch": {"flip_type": "off"}}},
            }
        ]
    },
}
# click Advanced Settings
{
    "method": "multipleRequest",
    "params": {
        "requests": [{"method": "getLdc", "params": {"image": {"name": "switch"}}}]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getLdc",
                "result": {
                    "image": {
                        "switch": {
                            ".name": "switch",
                            ".type": "switch_type",
                            "switch_mode": "common",
                            "schedule_start_time": "21600",
                            "schedule_end_time": "64800",
                            "rotate_type": "off",
                            "ldc": "off",
                            "flip_type": "off",
                            "night_vision_mode": "inf_night_vision",
                            "wtl_intensity_level": "5",
                        }
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}
# enable/disable the orange status LED
post_req = {
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setLedStatus",
                "params": {"led": {"config": {"enabled": "off"}}},
            }
        ]
    },
}
post_req = {
    "method": "multipleRequest",
    "params": {
        "requests": [
            {"method": "setLedStatus", "params": {"led": {"config": {"enabled": "on"}}}}
        ]
    },
}

# get sdcard status
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getSdCardStatus",
                "params": {"harddisk_manage": {"table": ["hd_info"]}},
            },
            {
                "method": "getCircularRecordingConfig",
                "params": {"harddisk_manage": {"name": ["harddisk"]}},
            },
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getSdCardStatus",
                "result": {
                    "harddisk_manage": {
                        "hd_info": [
                            {
                                "hd_info_1": {
                                    "disk_name": "1",
                                    "rw_attr": "r",
                                    "status": "offline",
                                    "detect_status": "offline",
                                    "write_protect": "0",
                                    "percent": "0",
                                    "type": "local",
                                    "record_duration": "0",
                                    "record_free_duration": "0",
                                    "record_start_time": "0",
                                    "loop_record_status": "0",
                                    "total_space": "0B",
                                    "free_space": "0B",
                                    "video_total_space": "0B",
                                    "video_free_space": "0B",
                                    "picture_total_space": "0B",
                                    "picture_free_space": "0B",
                                    "msg_push_total_space": "0B",
                                    "msg_push_free_space": "0B",
                                }
                            }
                        ]
                    }
                },
                "error_code": 0,
            },
            {
                "method": "getCircularRecordingConfig",
                "result": {
                    "harddisk_manage": {
                        "harddisk": {
                            ".name": "harddisk",
                            ".type": "storage",
                            "loop": "on",
                        }
                    }
                },
                "error_code": 0,
            },
        ]
    },
    "error_code": 0,
}
# get clock status
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getClockStatus",
                "params": {"system": {"name": "clock_status"}},
            },
            {"method": "getTimezone", "params": {"system": {"name": "basic"}}},
            {"method": "getDstRule", "params": {"system": {"name": "dst"}}},
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getClockStatus",
                "result": {
                    "system": {
                        "clock_status": {
                            "seconds_from_1970": 1636461602,
                            "local_time": "2021-11-09 12:40:02",
                        }
                    }
                },
                "error_code": 0,
            },
            {
                "method": "getTimezone",
                "result": {
                    "system": {
                        "basic": {
                            ".name": "basic",
                            ".type": "setting",
                            "timezone": "UTC-00:00",
                            "timing_mode": "ntp",
                            "zone_id": "Europe\/London",
                        }
                    }
                },
                "error_code": 0,
            },
            {
                "method": "getDstRule",
                "result": {
                    "system": {
                        "dst": {
                            ".name": "dst",
                            ".type": "dst",
                            "enabled": "1",
                            "synced": "0",
                            "has_rule": "0",
                            "dst_start_1": "---",
                            "dst_end_1": "---",
                            "dst_savings_1": "---",
                            "dst_start_2": "---",
                            "dst_end_2": "---",
                            "dst_savings_2": "---",
                            "dst_local_start": "---",
                            "dst_local_end": "---",
                            "dst_offset": "---",
                        }
                    }
                },
                "error_code": 0,
            },
        ]
    },
    "error_code": 0,
}
# set timezone for NTP
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setTimezone",
                "params": {
                    "system": {
                        "basic": {
                            "timing_mode": "ntp",
                            "timezone": "UTC-00:00",
                            "zone_id": "UTC",
                        }
                    }
                },
            }
        ]
    },
}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setTimezone",
                "params": {
                    "system": {
                        "basic": {
                            "timing_mode": "ntp",
                            "timezone": "UTC-00:00",
                            "zone_id": "Europe/London",
                        }
                    }
                },
            }
        ]
    },
}


## on screen display settings
### get info
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getOsd",
                "params": {
                    "OSD": {
                        "name": ["logo", "date", "week", "font"],
                        "table": ["label_info"],
                    }
                },
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getOsd",
                "result": {
                    "OSD": {
                        "logo": {
                            ".name": "logo",
                            ".type": "date_info",
                            "enabled": "on",
                            "x_coor": "0",
                            "y_coor": "9150",
                        },
                        "date": {
                            ".name": "date",
                            ".type": "date_info",
                            "enabled": "on",
                            "x_coor": "0",
                            "y_coor": "0",
                        },
                        "week": {
                            ".name": "week",
                            ".type": "date_info",
                            "enabled": "off",
                            "x_coor": "6000",
                            "y_coor": "500",
                        },
                        "font": {
                            ".name": "font",
                            ".type": "font_info",
                            "display": "ntnb",
                            "size": "auto",
                            "color_type": "auto",
                            "color": "white",
                        },
                        "label_info": [
                            {
                                "label_info_1": {
                                    ".name": "label_info_1",
                                    ".type": "label_info",
                                    "enabled": "off",
                                    "text": "TP IPC",
                                    "x_coor": "0",
                                    "y_coor": "700",
                                }
                            },
                            {
                                "label_info_2": {
                                    ".name": "label_info_2",
                                    ".type": "label_info",
                                    "enabled": "off",
                                    "text": "自定义字符1",
                                    "x_coor": "1000",
                                    "y_coor": "4000",
                                }
                            },
                            {
                                "label_info_3": {
                                    ".name": "label_info_3",
                                    ".type": "label_info",
                                    "enabled": "off",
                                    "text": "自定义字符2",
                                    "x_coor": "1000",
                                    "y_coor": "6000",
                                }
                            },
                        ],
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}
### disable/enable logo
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setOsd",
                "params": {
                    "OSD": {"logo": {"enabled": "off", "x_coor": "0", "y_coor": "9150"}}
                },
            }
        ]
    },
}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setOsd",
                "params": {
                    "OSD": {"logo": {"enabled": "on", "x_coor": "0", "y_coor": "9150"}}
                },
            }
        ]
    },
}
### set the display text
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setOsd",
                "params": {
                    "OSD": {
                        "date": {"enabled": "on", "x_coor": "0", "y_coor": "0"},
                        "week": {"enabled": "off", "x_coor": "0", "y_coor": "0"},
                        "font": {
                            "color": "white",
                            "color_type": "auto",
                            "display": "ntnb",
                            "size": "auto",
                        },
                        "label_info_1": {
                            "enabled": "on",
                            "text": "bob",
                            "x_coor": "0",
                            "y_coor": "500",
                        },
                    }
                },
            }
        ]
    },
}

## turn diagnostics logging to SDcard on (should call checkDiagnoseStatus after, if it returns "stopped" then could be no SD card inserted)
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setDiagnoseMode",
                "params": {"system": {"sys": {"diagnose_mode": "on"}}},
            }
        ]
    },
}

{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "checkDiagnoseStatus",
                "params": {"system": {"check_diagnose_status": ""}},
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "checkDiagnoseStatus",
                "result": {"status": "off"},
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {"method": "getDiagnoseMode", "params": {"system": {"name": "sys"}}}
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getDiagnoseMode",
                "result": {
                    "system": {
                        "sys": {
                            ".name": "sys",
                            ".type": "system",
                            "diagnose_mode": "off",
                            "makeroom_status": "0",
                            "append_dns": "0.0.0.0",
                            "alias": "TC65 1.0",
                            "is_factory": "0",
                            "network_type": "WiFi",
                            "dev_alias": "mycamera2",
                            "hostname": "TC65",
                        }
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}
# get user id
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {"method": "getUserID", "params": {"system": {"get_user_id": "null"}}}
        ]
    },
}
{
    "result": {
        "responses": [
            {"method": "getUserID", "result": {"user_id": 1}, "error_code": 0}
        ]
    },
    "error_code": 0,
}

# get network settings
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getConnectionType",
                "params": {"network": {"get_connection_type": ["null"]}},
            },
            {"method": "getDeviceIpAddress", "params": {"network": {"name": ["wan"]}}},
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getConnectionType",
                "result": {
                    "link_type": "wifi",
                    "ssid": "man",
                    "rssi": "4",
                    "rssiValue": -27,
                },
                "error_code": 0,
            },
            {
                "method": "getDeviceIpAddress",
                "result": {
                    "network": {
                        "wan": {
                            ".name": "wan",
                            ".type": "interface",
                            "ifname": "br-wan",
                            "type": "bridge",
                            "wan_type": "dhcp",
                            "speed_duplex": "auto",
                            "proto": "dhcp",
                            "mtu": "1480",
                            "auto": "1",
                            "netmask": "255.255.255.0",
                            "macaddr": "9C:A2:F4:C0:E9:CE",
                            "fac_macaddr": "9C:A2:F4:C0:E9:CE",
                            "ipaddr": "192.168.1.178",
                            "gateway": "192.168.1.1",
                            "dns": "192.168.1.1",
                        }
                    }
                },
                "error_code": 0,
            },
        ]
    },
    "error_code": 0,
}

# first click on detection settings (detection & alerts)
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getDetectionConfig",
                "params": {"motion_detection": {"name": ["motion_det"]}},
            },
            {
                "method": "getAlertConfig",
                "params": {"msg_alarm": {"name": ["chn1_msg_alarm_info"]}},
            },
            {
                "method": "getMsgPushConfig",
                "params": {"msg_push": {"name": ["chn1_msg_push_info"]}},
            },
            {
                "method": "getPersonDetectionConfig",
                "params": {"people_detection": {"name": ["detection"]}},
            },
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getDetectionConfig",
                "result": {
                    "motion_detection": {
                        "motion_det": {
                            ".name": "motion_det",
                            ".type": "on_off",
                            "enabled": "on",
                            "sensitivity": "medium",
                            "digital_sensitivity": "50",
                        }
                    }
                },
                "error_code": 0,
            },
            {
                "method": "getAlertConfig",
                "result": {
                    "msg_alarm": {
                        "chn1_msg_alarm_info": {
                            ".name": "chn1_msg_alarm_info",
                            ".type": "info",
                            "enabled": "off",
                            "alarm_type": "0",
                            "light_type": "1",
                            "alarm_mode": ["sound", "light"],
                            "sound_alarm_enabled": "off",
                            "light_alarm_enabled": "off",
                        }
                    }
                },
                "error_code": 0,
            },
            {
                "method": "getMsgPushConfig",
                "result": {
                    "msg_push": {
                        "chn1_msg_push_info": {
                            ".name": "chn1_msg_push_info",
                            ".type": "on_off",
                            "notification_enabled": "on",
                            "rich_notification_enabled": "off",
                        }
                    }
                },
                "error_code": 0,
            },
            {
                "method": "getPersonDetectionConfig",
                "result": {
                    "people_detection": {
                        "detection": {
                            ".name": "detection",
                            ".type": "on_off",
                            "enabled": "off",
                        }
                    }
                },
                "error_code": 0,
            },
        ]
    },
    "error_code": 0,
}
## click on Motion Detection
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getDetectionConfig",
                "params": {
                    "motion_detection": {
                        "name": ["motion_det"],
                        "table": ["region_info"],
                    }
                },
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getDetectionConfig",
                "result": {
                    "motion_detection": {
                        "motion_det": {
                            ".name": "motion_det",
                            ".type": "on_off",
                            "enabled": "on",
                            "sensitivity": "medium",
                            "digital_sensitivity": "50",
                        },
                        "region_info": [
                            {
                                "region_info_1": {
                                    ".name": "region_info_1",
                                    ".type": "region_info",
                                    "height": "10000",
                                    "width": "10000",
                                    "x_coor": "0",
                                    "y_coor": "0",
                                }
                            }
                        ],
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}
### here turn motion detection off
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setDetectionConfig",
                "params": {
                    "motion_detection": {
                        "motion_det": {"digital_sensitivity": "50", "enabled": "off"}
                    }
                },
            }
        ]
    },
}
### here turn motion detection on
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setDetectionConfig",
                "params": {
                    "motion_detection": {
                        "motion_det": {"digital_sensitivity": "50", "enabled": "on"}
                    }
                },
            }
        ]
    },
}
### set sensitivity low
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setDetectionConfig",
                "params": {
                    "motion_detection": {
                        "motion_det": {"digital_sensitivity": "20", "enabled": "on"}
                    }
                },
            }
        ]
    },
}
### set sensitivity medium
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setDetectionConfig",
                "params": {
                    "motion_detection": {
                        "motion_det": {"digital_sensitivity": "50", "enabled": "on"}
                    }
                },
            }
        ]
    },
}
### set sensitivity high
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setDetectionConfig",
                "params": {
                    "motion_detection": {
                        "motion_det": {"digital_sensitivity": "80", "enabled": "on"}
                    }
                },
            }
        ]
    },
}