import ipaddress
import socket
import typing as t
from multiprocessing import Pool


def scan_single_ip_is_camera(
    ip, identification_ports: t.Iterable[int] = [443, 554, 2020, 8800]
):
    # determination of a likely camera is done based upon a device's open ports
    ports_open = True
    for port in identification_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.2)
            result = sock.connect_ex((ip, port))
            sock.close()
            if result == 0:
                ports_open = ports_open & True
            else:
                ports_open = False
        except (socket.timeout, socket.gaierror, socket.error):
            ports_open = False
        if not ports_open:
            break
    if ports_open:
        return ip


def scan_ips_for_cameras(ips, pool_size: int = 20):
    # given list of ip addresses, return a list of ip addresses which are identified as cameras
    with Pool(processes=pool_size) as pool:
        results = pool.map(scan_single_ip_is_camera, ips)
        pool.close()
    return [r for r in results if r]


def generate_ip_range(ip, size: int = 24):
    # TODO remove the str conversion here and move to consumers
    return (str(ip) for ip in ipaddress.IPv4Network(f"{ip}/{size}", False))


def check_ip_address_format(s: str):
    try:
        ipaddress.ip_address(s)
        return True
    except ValueError:
        return False
