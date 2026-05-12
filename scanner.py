"""
Port scanning function

This script provides functions for performing basic network reconnaissance, i.e. determining
if a host/port pair is listening.

Utilizes socket library.

Author: Isaac Colletti
Last updated: 5/11/2026
"""

import socket


def scan_port(host, port):
    """
    Attempts to connect to a specific port on a specific host.

    :param host: str
        Target hostname or IP address
    :param port: int
        Target port number
    :return: dict
        Scan results
    """

    result_data = {
        "host" : host,
        "port" : port,
        "open" : False,
        "error" : None
    }

    try:
        # create a TCP socket using IPv4
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # prevent long scans on unreachable ports
        sock.settimeout(1)

        # attempt connection
        result = sock.connect_ex((host, port))

        # close socket
        sock.close()

        # successful connection
        if result == 0:
            result_data["open"] = True

    except socket.gaierror:
        result_data["error"] = "Hostname could not be resolved"

    except socket.timeout:
        result_data["error"] = "Connection timed out"

    except socket.error as e:
        result_data["error"] = str(e)

    return result_data


def scan_port_range(host, start_port, end_port):
    """
    Scans a range of ports on a target host.

    :param host: str
        Target hostname or IP address
    :param start_port: int
        Start port for the range
    :param end_port: int
        Ending port number for the range
    :return: list
        list of dictionaries of scan results
    """

    results_list = []

    # scan each port in the range and add to results_list
    for port in range(start_port, end_port + 1):
        result = scan_port(host, port)
        results_list.append(result)

    return results_list
