# Tapo Camera Tools

Based upon the TC65
Commands for interacting with a tapo camera

## Notes
Requires python 3.8 for the time being due to SSL certificate requirements being made more strict in later versions

Have not yet looked to use later version and adjust how the SSL certificates are checked

`poetry env use 3.8`

## Todo?
- [ ] Implement additional logged methods (see `todo/implemented.py` for payload log)
- [ ] Items marked TODO
- [ ] Change to use JSONWizard
- [ ] Clean everything up
- [ ] Error handling
- [ ] UI
- [ ] Async
- [ ] Tests

## Tools
```
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help                  Show this message and exit.

Commands:
  find-cameras      Scan the /24 block of given interface for potential...
  provision-camera  Provision a fresh camera so that it is minimally...
```

### Interactive Provisioning
Provision a fresh (recently reset or new) camera following the steps undertaken by the 'companion app' but only through local communication with the camera
```
poetry run python main.py provision-camera
Usage: main.py provision-camera [OPTIONS]

Provision a fresh camera so that it is minimally available for rtsp

Options:
  --camera-password TEXT      Password to set for controlling the camera (e.g. via this tool)  [required]
  --camera-alias TEXT         Set camera name (not for login, but helpful in device identification)
  --wifi-name TEXT            ESSID (name) of network to connect the camera to for regular operation  [required]
  --wifi-password TEXT        Password of network to connect the camera to for regular operation  [required]
  --third-user-name TEXT      Username to set for connecting to the camera after setup (rtsp streams)  [required]
  --third-user-password TEXT  Password to set for connecting to the camera after setup (rtsp streams)  [required]
  --timezone-id TEXT          Timezone identifier e.g. America/New_Yor
  --format-sd                 Whether to re-format (wipe) the SD card inserted to the camera on setup
```

### Find IP addresses of tapo cameras on the network
Presents a list of network interfaces to search for (if connected to multiple networks) and scans for potential and confirmed cameras.

Potential is based on open ports. Confirmation is based on responses.
```
Usage: main.py find-cameras [OPTIONS]

Options:
  --camera-password TEXT      If known, use this password to confirm the device is a tapo camera and return the alias
```