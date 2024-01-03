# check for firmware update
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "checkFirmwareVersionByCloud",
                "params": {"cloud_config": {"check_fw_version": "null"}},
            },
            {
                "method": "getCloudConfig",
                "params": {"cloud_config": {"name": ["upgrade_info"]}},
            },
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "checkFirmwareVersionByCloud",
                "result": {},
                "error_code": -51219,
            },
            {
                "method": "getCloudConfig",
                "result": {
                    "cloud_config": {
                        "upgrade_info": {
                            ".name": "upgrade_info",
                            ".type": "cloud_reply",
                        }
                    }
                },
                "error_code": 0,
            },
        ]
    },
    "error_code": 0,
}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getFirmwareUpdateStatus",
                "params": {"cloud_config": {"name": "upgrade_status"}},
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getFirmwareUpdateStatus",
                "result": {
                    "cloud_config": {
                        "upgrade_status": {
                            "state": "normal",
                            "lastUpgradingSuccess": False,
                        }
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}


### set the region (not adding multiple regions)
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "addDetectionRegion",
                "params": {
                    "motion_detection": {
                        "add_md_regions": {
                            "region_info": [
                                {
                                    "height": "10000",
                                    "width": "2235",
                                    "x_coor": "0",
                                    "y_coor": "0",
                                }
                            ]
                        }
                    }
                },
            }
        ]
    },
}
### set a different region (covering whole area) (not adding multiple regions)
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "addDetectionRegion",
                "params": {
                    "motion_detection": {
                        "add_md_regions": {
                            "region_info": [
                                {
                                    "height": "10000",
                                    "width": "10000",
                                    "x_coor": "0",
                                    "y_coor": "0",
                                }
                            ]
                        }
                    }
                },
            }
        ]
    },
}
### set a different region (2 regions)
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "addDetectionRegion",
                "params": {
                    "motion_detection": {
                        "add_md_regions": {
                            "region_info": [
                                {
                                    "height": "5398",
                                    "width": "3750",
                                    "x_coor": "5518",
                                    "y_coor": "3967",
                                },
                                {
                                    "height": "4094",
                                    "width": "3932",
                                    "x_coor": "680",
                                    "y_coor": "1068",
                                },
                            ]
                        }
                    }
                },
            }
        ]
    },
}
## click on AI Detection / person detection
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setPersonDetectionConfig",
                "params": {"people_detection": {"detection": {"enabled": "on"}}},
            }
        ]
    },
}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setPersonDetectionConfig",
                "params": {"people_detection": {"detection": {"enabled": "off"}}},
            }
        ]
    },
}
## click on line-crossing detection
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getLinecrossingDetectionConfig",
                "params": {
                    "linecrossing_detection": {"name": ["detection", "arming_schedule"]}
                },
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getLinecrossingDetectionConfig",
                "result": {
                    "linecrossing_detection": {
                        "detection": {
                            ".name": "detection",
                            ".type": "on_off",
                            "enabled": "off",
                        },
                        "arming_schedule": {
                            ".name": "arming_schedule",
                            ".type": "plan",
                            "monday": '["0000-2400"]',
                            "tuesday": '["0000-2400"]',
                            "wednesday": '["0000-2400"]',
                            "thursday": '["0000-2400"]',
                            "friday": '["0000-2400"]',
                            "saturday": '["0000-2400"]',
                            "sunday": '["0000-2400"]',
                        },
                    }
                },
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
            {
                "method": "getLinecrossingDetectionRegion",
                "params": {"linecrossing_detection": {"table": ["region_info"]}},
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getLinecrossingDetectionRegion",
                "result": {"linecrossing_detection": {"region_info": []}},
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}
### turn it on
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setLinecrossingDetectionConfig",
                "params": {"linecrossing_detection": {"detection": {"enabled": "on"}}},
            }
        ]
    },
}
### turn it off
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setLinecrossingDetectionConfig",
                "params": {"linecrossing_detection": {"detection": {"enabled": "off"}}},
            }
        ]
    },
}
### set some boundary settings (lines which trigger crossing) {both, AtoB, BtoA}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "addLinecrossingDetectionRegion",
                "params": {
                    "linecrossing_detection": {
                        "add_regions": {
                            "region_info": [
                                {
                                    "direction": "both",
                                    "pt1_x": "303",
                                    "pt1_y": "8086",
                                    "pt2_x": "9676",
                                    "pt2_y": "8179",
                                    "sensitivity": "50",
                                },
                                {
                                    "direction": "AtoB",
                                    "pt1_x": "1171",
                                    "pt1_y": "6651",
                                    "pt2_x": "1373",
                                    "pt2_y": "1851",
                                    "sensitivity": "50",
                                },
                                {
                                    "direction": "AtoB",
                                    "pt1_x": "7414",
                                    "pt1_y": "2978",
                                    "pt2_x": "7363",
                                    "pt2_y": "6836",
                                    "sensitivity": "50",
                                },
                            ]
                        }
                    }
                },
            }
        ]
    },
}
### set schedule (interface on phone only allows 1h steps)
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setLinecrossingDetectionSchedule",
                "params": {
                    "linecrossing_detection": {
                        "arming_schedule": {
                            "friday": '["0800-2400"]',
                            "monday": '["0000-0500","1300-2200","2300-2400"]',
                            "saturday": '["0000-2400"]',
                            "sunday": '["0000-2300"]',
                            "thursday": '["0000-0300","0400-0500","0600-2400"]',
                            "tuesday": '["0000-2400"]',
                            "wednesday": '["0000-0900","1000-1800","2200-2400"]',
                        }
                    }
                },
            }
        ]
    },
}
### set schedule so all disabled
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setLinecrossingDetectionSchedule",
                "params": {
                    "linecrossing_detection": {
                        "arming_schedule": {
                            "friday": "[]",
                            "monday": "[]",
                            "saturday": "[]",
                            "sunday": "[]",
                            "thursday": "[]",
                            "tuesday": "[]",
                            "wednesday": "[]",
                        }
                    }
                },
            }
        ]
    },
}
## click on area intrusion detection
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getIntrusionDetectionConfig",
                "params": {
                    "intrusion_detection": {"name": ["detection", "arming_schedule"]}
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
                "method": "getIntrusionDetectionRegion",
                "params": {"intrusion_detection": {"table": ["region_info"]}},
            }
        ]
    },
}
### turn on
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setIntrusionDetectionConfig",
                "params": {"intrusion_detection": {"detection": {"enabled": "on"}}},
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
                "method": "setIntrusionDetectionConfig",
                "params": {"intrusion_detection": {"detection": {"enabled": "off"}}},
            }
        ]
    },
}
### set regions
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "addIntrusionDetectionRegion",
                "params": {
                    "intrusion_detection": {
                        "add_regions": {
                            "region_info": [
                                {
                                    "pt3_x": "5670",
                                    "pt3_y": "7282",
                                    "pt1_x": "0",
                                    "pt1_y": "942",
                                    "percentage": "0",
                                    "pt4_x": "0",
                                    "pt4_y": "7282",
                                    "pt2_x": "5670",
                                    "pt2_y": "942",
                                    "sensitivity": "50",
                                    "threshold": "0",
                                },
                                {
                                    "pt3_x": "10000",
                                    "pt3_y": "3586",
                                    "pt1_x": "6250",
                                    "pt1_y": "670",
                                    "percentage": "0",
                                    "pt4_x": "6250",
                                    "pt4_y": "3586",
                                    "pt2_x": "10000",
                                    "pt2_y": "670",
                                    "sensitivity": "50",
                                    "threshold": "0",
                                },
                            ]
                        }
                    }
                },
            }
        ]
    },
}
### set schedule
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setIntrusionDetectionSchedule",
                "params": {
                    "intrusion_detection": {
                        "arming_schedule": {
                            "friday": '["0000-2400"]',
                            "monday": '["0000-1000","1900-2100"]',
                            "saturday": '["0000-2400"]',
                            "sunday": '["0000-2400"]',
                            "thursday": '["0000-2400"]',
                            "tuesday": '["0000-2400"]',
                            "wednesday": "[]",
                        }
                    }
                },
            }
        ]
    },
}
## tamper detection (someone blocks camera)
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getTamperDetectionConfig",
                "params": {"tamper_detection": {"name": ["tamper_det"]}},
            }
        ]
    },
}
### turn on
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setTamperDetectionConfig",
                "params": {
                    "tamper_detection": {
                        "tamper_det": {
                            "digital_sensitivity": "50",
                            "enabled": "on",
                            "sensitivity": "medium",
                        }
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
                "method": "setTamperDetectionConfig",
                "params": {
                    "tamper_detection": {
                        "tamper_det": {
                            "digital_sensitivity": "50",
                            "enabled": "on",
                            "sensitivity": "low",
                        }
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
                "method": "setTamperDetectionConfig",
                "params": {
                    "tamper_detection": {
                        "tamper_det": {
                            "digital_sensitivity": "50",
                            "enabled": "on",
                            "sensitivity": "high",
                        }
                    }
                },
            }
        ]
    },
}
### turn  off
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setTamperDetectionConfig",
                "params": {
                    "tamper_detection": {
                        "tamper_det": {
                            "digital_sensitivity": "50",
                            "enabled": "off",
                            "sensitivity": "medium",
                        }
                    }
                },
            }
        ]
    },
}
## activity notifications
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getMsgPushConfig",
                "params": {"msg_push": {"name": ["chn1_msg_push_info"]}},
            }
        ]
    },
}
{
    "result": {
        "responses": [
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
            }
        ]
    },
    "error_code": 0,
}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getMsgPushPlan",
                "params": {"msg_push_plan": {"name": ["chn1_msg_push_plan"]}},
            }
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getMsgPushPlan",
                "result": {
                    "msg_push_plan": {
                        "chn1_msg_push_plan": {
                            ".name": "chn1_msg_push_plan",
                            ".type": "plan",
                            "enabled": "off",
                            "push_plan_1": "0900-1700,127",
                        }
                    }
                },
                "error_code": 0,
            }
        ]
    },
    "error_code": 0,
}
### turn off
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setMsgPushConfig",
                "params": {
                    "msg_push": {
                        "chn1_msg_push_info": {
                            "notification_enabled": "off",
                            "rich_notification_enabled": "off",
                        }
                    }
                },
            }
        ]
    },
}
### turn on
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setMsgPushConfig",
                "params": {
                    "msg_push": {
                        "chn1_msg_push_info": {
                            "notification_enabled": "on",
                            "rich_notification_enabled": "off",
                        }
                    }
                },
            }
        ]
    },
}
### set to only send in the day, but all days of the week
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setMsgPushPlan",
                "params": {
                    "msg_push_plan": {
                        "chn1_msg_push_plan": {
                            "enabled": "on",
                            "push_plan_1": "0800-2000,127",
                        }
                    }
                },
            }
        ]
    },
}
### set to send at any time, all days of the week
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setMsgPushPlan",
                "params": {
                    "msg_push_plan": {
                        "chn1_msg_push_plan": {
                            "enabled": "off",
                            "push_plan_1": "0000-0000,127",
                        }
                    }
                },
            }
        ]
    },
}
### set to send at any time, SMTWXFS: the days are determined by adding the numbers together where each number represents a day which is enabled
### Sunday: 1, Mon: 2, Tue: 4, Wed: 8, Thu: 16, Fri: 32, Sun: 64   e.g. for Mon&Wed would put 10, Whole week 127
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setMsgPushPlan",
                "params": {
                    "msg_push_plan": {
                        "chn1_msg_push_plan": {
                            "enabled": "on",
                            "push_plan_1": "0900-1700,111",
                        }
                    }
                },
            }
        ]
    },
}

## have the camera make an alarm when motion detected
### get info
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
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "getAlertPlan",
                "params": {"msg_alarm_plan": {"name": ["chn1_msg_alarm_plan"]}},
            }
        ]
    },
}
### turn on
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setAlertConfig",
                "params": {
                    "msg_alarm": {
                        "chn1_msg_alarm_info": {
                            "alarm_type": "0",
                            "enabled": "on",
                            "light_type": "0",
                            "alarm_mode": ["light", "sound"],
                        }
                    }
                },
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
                "method": "setAlertConfig",
                "params": {
                    "msg_alarm": {
                        "chn1_msg_alarm_info": {
                            "alarm_type": "0",
                            "enabled": "off",
                            "light_type": "0",
                            "alarm_mode": ["light", "sound"],
                        }
                    }
                },
            }
        ]
    },
}
### set alert only at given times/days
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setAlertPlan",
                "params": {
                    "msg_alarm_plan": {
                        "chn1_msg_alarm_plan": {
                            "enabled": "on",
                            "alarm_plan_1": "0800-2000,127",
                        }
                    }
                },
            }
        ]
    },
}
### turn off alerting only given days/times and always alert
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setAlertPlan",
                "params": {
                    "msg_alarm_plan": {
                        "chn1_msg_alarm_plan": {
                            "enabled": "off",
                            "alarm_plan_1": "0000-0000,127",
                        }
                    }
                },
            }
        ]
    },
}


## record audio
### disable audio in recordings
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setRecordAudio",
                "params": {"audio_config": {"record_audio": {"enabled": "off"}}},
            }
        ]
    },
}
### enable audio in recordings
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setRecordAudio",
                "params": {"audio_config": {"record_audio": {"enabled": "on"}}},
            }
        ]
    },
}
## set powerline frequency (auto, 50, 60)
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setLightFrequencyInfo",
                "params": {"image": {"common": {"light_freq_mode": "auto"}}},
            }
        ]
    },
}
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "setLightFrequencyInfo",
                "params": {"image": {"common": {"light_freq_mode": "60"}}},
            }
        ]
    },
}


# search for recorded videos within given period or by if flagged detection
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {
                "method": "searchDateWithVideo",
                "params": {
                    "playback": {
                        "search_year_utility": {
                            "channel": [0],
                            "end_date": "20211130",
                            "start_date": "20211101",
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
                "method": "searchVideoWithUTC",
                "params": {
                    "playback": {
                        "search_video_with_utc": {
                            "channel": 0,
                            "end_index": 99,
                            "end_time": 1636502399,
                            "id": 1,
                            "start_index": 0,
                            "start_time": 1636416000,
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
                "method": "searchDetectionList",
                "params": {
                    "playback": {
                        "search_detection_list": {
                            "channel": 0,
                            "end_index": 99,
                            "end_time": 1636502399,
                            "start_index": 0,
                            "start_time": 1636416000,
                        }
                    }
                },
            }
        ]
    },
}

# auto reboot schedule
{
    "method": "multipleRequest",
    "params": {
        "requests": [
            {"method": "getReboot", "params": {"timing_reboot": {"name": ["reboot"]}}}
        ]
    },
}
{
    "result": {
        "responses": [
            {
                "method": "getReboot",
                "result": {
                    "timing_reboot": {
                        "reboot": {
                            ".name": "reboot",
                            ".type": "on_off",
                            "enabled": "off",
                            "day": "0",
                            "time": "03:00:00",
                            "random_range": "30",
                            "last_reboot_time": "0",
                        }
                    }
                },
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
            {
                "method": "setReboot",
                "params": {
                    "timing_reboot": {
                        "reboot": {
                            "day": "0",
                            "enabled": "on",
                            "random_range": 30,
                            "time": "03:30:00",
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
                "method": "setReboot",
                "params": {
                    "timing_reboot": {
                        "reboot": {
                            "day": "0",
                            "enabled": "off",
                            "random_range": 30,
                            "time": "03:30:00",
                        }
                    }
                },
            }
        ]
    },
}