"""
Network reconnaissance tool

Utilizes scan_port function to scan a user-provided port range on a user-provided host.

Author: Isaac Colletti
Last Updated: 5/11/2026
"""

from scanner import scan_port_range

from utils import print_scan_results, verify_port_range, get_integer_input


def main():
    """
    Main entry point for the network reconnaissance tool

    :return: None
    """

    print("=== Network recon tool ===")

    # Get target values from user
    host_name = input("Enter target host: ")
    start_port = get_integer_input("Enter starting port: ")
    end_port = get_integer_input("Enter ending port: ")

    # Verify range
    start_port, end_port = verify_port_range(start_port, end_port)

    # Scan over the specified range and print results
    results = scan_port_range(host_name, start_port, end_port)
    print_scan_results(results)


if __name__ == "__main__":
    main()