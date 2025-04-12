import uuid
import tcp_connection
import ipaddress
import typing


class Disk(tcp_connection.TcpConnection):

    def __init__(self, disk_uuid: uuid.UUID, ip_address: ipaddress.IPv4Address, port: int) -> None:
        super().__init__(ip_address, port)
        self.uuid: uuid.UUID = disk_uuid

    def online(self):
        """
            Bring the Current Disk online
        :return:
        """
        self._error_check(self._send_tcp(f"get|disk|str({self.uuid})|1"))

    def offline(self):
        """
            Take the Disk Offline
            :return:
        """
        self._error_check(self._send_tcp(f"closedisk|{str(self.uuid)}"))

    def get_files_in_location(self) -> typing.List[str]:
        """
            Get all the from the specified location
        :param location:
        :return:
        """
        return self._error_check_list(self._send_tcp(f"get|files|{self.uuid}|1"))