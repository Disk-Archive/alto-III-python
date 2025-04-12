import ipaddress
import socket
import typing

import error


class TcpConnection(object):

    def __init__(self, ip_address: ipaddress.IPv4Address, port: int) -> None:
        self.ip_address = ip_address
        self.port = port
        self.disks = []

    def _send_tcp(self, message: str, timeout: int = 5) -> str:
        try:
            with socket.create_connection((str(self.ip_address), self.port), timeout=timeout) as sock:
                sock.sendall((message + '\n').encode())
                response = sock.recv(4096)
                return response.decode()
        except Exception as e:
            return f"Error: {e}"

    def _check_for_alto_errors(self, alto_return_string: str) -> str:
        print(alto_return_string)
        parts = alto_return_string.split("|")

        if len(parts) <= 1:
            raise error.AltoException("Unrecognised alto message")

        if parts[0] == "0":
            raise error.AltoException("Alto returned a zero error code")

        return " ".join(parts[1:])