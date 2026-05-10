"""
Network reconnaissance tool

Utilizes scan_port function to scan a user-provided port number on a user-provided host.

Author: Isaac Colletti
Last Updated: 5/10/2026
"""

from scanner import scan_port


def main():
    """
    Main entry point for the network reconnaissance tool

    :return: None
    """

    print("=== Network recon tool ===")

    # Get target values from user
    host_name = input("Enter target host: ")
    port_number = int(input("Enter target port: "))

    # scan host/port pair
    results = scan_port(host_name, port_number)

    # print results
    print("=== Scan Results ===")
    print(f"Host: {results['host']}\nPort: {results['port']}\nOpen: {results['open']}")
    if results['error'] is not None:
        print(f"Error: {results['error']}")

if __name__ == "__main__":
    main()



