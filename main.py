"""
Network reconnaissance tool

Performs concurrent port scans on a user-provided port range on a user-provided host.

Determines whether ports are accepting TCP connections.

Author: Isaac Colletti
Last Updated: 5/12/2026
"""

from scanner import scan_port_range

from utils import print_scan_results, verify_port_range, get_integer_input, verify_hostname

import time


def main():
    """
    Main entry point for the network reconnaissance tool

    :return: None
    """

    print("\n=== Network recon tool ===\n")

    # Get target values from user
    hostname = input("Enter target host: ")
    while not verify_hostname(hostname):
        print("Hostname could not be resolved.")
        hostname = input("Enter target host: ")
    start_port = get_integer_input("Enter starting port: ")
    end_port = get_integer_input("Enter ending port: ")

    # Verify range
    start_port, end_port = verify_port_range(start_port, end_port)

    # Scan over the specified range and print results
    try:
        print("\nScan in progress...\n")
        start_time = time.time()
        results = scan_port_range(hostname, start_port, end_port)
        scan_duration = time.time() - start_time
        print_scan_results(results, scan_duration)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user - Python may take a moment to clean up"
              " active threads. Press Ctrl+c again to force termination.\n")


if __name__ == "__main__":
    main()