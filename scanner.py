import socket
from ssl import socket_error


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