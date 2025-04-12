import uuid
import tcp_connection
import ipaddress


class Disk(tcp_connection.TcpConnection):

    def __init__(self, disk_uuid: uuid.UUID, ip_address: ipaddress.IPv4Address, port: int) -> None:
        super().__init__(ip_address, port)
        self.uuid: uuid.UUID = disk_uuid

    def online(self):
        """
            Bring the Current Disk online
        :return:
        """
        self._error_check(self._send_tcp(f"opendisk|{str(self.uuid)}"))

    def offline(self):
        """
            Take the Disk Offline
            :return:
        """
        self._error_check(self._send_tcp(f"closedisk|{str(self.uuid)}"))