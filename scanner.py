"""
Port scanning function

This script provides functions for performing basic network reconnaissance, i.e. determining
if a host/port pair is listening.

Utilizes socket library.

Author: Isaac Colletti
Last updated: 5/12/2026
"""

import socket

import concurrent.futures


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
        "host": host,
        "port": port,
        "open": False,
        "error": None
    }

    sock = None

    try:
        # create a TCP socket using IPv4
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # prevent long scans on unreachable ports
        sock.settimeout(1)

        # attempt connection
        result = sock.connect_ex((host, port))

        # successful connection
        if result == 0:
            result_data["open"] = True

    except socket.gaierror:
        result_data["error"] = "Hostname could not be resolved"

    except socket.timeout:
        result_data["error"] = "Connection timed out"

    except socket.error as e:
        result_data["error"] = str(e)

    finally:
        if sock is not None:
            sock.close()

    return result_data


def scan_port_range(host, start_port, end_port):
    """
    Scans a range of ports concurrently on a target host.

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

    # Create pool of worker threads
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=100)

    try:
        # submit scans for each port and map each to a Future object
        future_to_port = {
            executor.submit(scan_port, host, port): port
            for port in range(start_port, end_port + 1)
        }

        # get results as they finish
        for future in concurrent.futures.as_completed(future_to_port):
            results_list.append(future.result())

    finally:
        # Begin cleanup without waiting for all worker threads to finish
        executor.shutdown(wait=False)

    return results_list