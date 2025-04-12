import uuid
import tcp_connection
import ipaddress


class Disk(tcp_connection.TcpConnection):

    def __init__(self, ip_address: ipaddress.IPv4Address, port: int) -> None:
        super().__init__(ip_address, port)

        self.id: uuid.UUID

    def online(self):
        """
            Bring the Current Disk online
        :return:
        """
        pass

    def offline(self):
        """
            Take the Disk Offline
            :return:
        """
        pass