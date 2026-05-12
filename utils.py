"""
Helper functions for main.py

Author: Isaac Colletti
Last Updated: 5/11/2026
"""

def print_scan_results(results_list):
    """
    Prints the results of a scan over a range.

    :param results_list: list
        list of dictionaries that each contain the results of a particular port scan
    :return: None
    """

    # Get user print preferences
    print_selector = get_integer_input("Type 1 to only show open ports, 2 to show all "
                                       "scan results: ")
    while print_selector not in (1, 2):
        print_selector = get_integer_input("Only enter values 1 or 2: ")

    # Print results based on user preferences
    for result in results_list:
        if print_selector == 1:
            if result['open']:
                print_individual_scan(result)

        elif print_selector == 2:
            print_individual_scan(result)

    print("=== Scan Complete ===")


def print_individual_scan(result):
    """
    Prints the results of an individual scan

    :param result: dict
        contains the results of an individual scan
    :return: None
    """

    if result['error'] is None:
        print(f"Port: {result['port']} | Open: {result['open']}")

    else:
        print(f"Port: {result['port']} | Error: {result['error']}")


def verify_port_range(start_port, end_port):
    """
    Helper function to verify range of TCP ports.

    :param start_port: int
        starting port for scan
    :param end_port: int
        ending port for scan
    :return: tuple
        validated (start_port, end_port)
    """
    while start_port > end_port or start_port < 0 or end_port > 65535:
        print("Starting port must be less than or equal to ending port, and values must be in"
              "range [0, 65535].")

        start_port = get_integer_input("Enter starting port: ")
        end_port = get_integer_input("Enter ending port: ")

    return start_port, end_port


def get_integer_input(prompt):
    """
    Ensures user input is an int

    :param prompt: str
        user prompt for input
    :return: int
        valid int
    """

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer: ")