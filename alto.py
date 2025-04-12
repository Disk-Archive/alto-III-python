import ipaddress
import tcp_connection
import disk


class AltoIII(tcp_connection.TcpConnection):

    """
        The Alto III object represents an Alto III Head, you can control the
        Alto operations by instantiating a new Alto III object.
    """

    def __init__(self, ip_address: ipaddress.IPv4Address, port: int) -> None:
        super().__init__(ip_address, port)
        self.disks: [disk.Disk] = []

    @property
    def system_name(self) -> str:
        """
        Gets the system name
        :return:
        """
        return self._check_for_alto_errors(self._send_tcp("get|system_name"))

    @system_name.setter
    def system_name(self, system_name: str) -> None:
        pass

    @property
    def system_serial(self) -> str:
        return self._check_for_alto_errors(self._send_tcp("get|system_serial"))

    def get_disk_with_free_space(self, file_size: int) -> disk.Disk:
        """
            Get a disk with enough free space to contain the given file_size in bytes
        :param file_size:
        :return:
        """
        pass