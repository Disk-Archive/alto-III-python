import ipaddress
import uuid
import tcp_connection
import disk
import typing
import group


class AltoIII(tcp_connection.TcpConnection):
    """
    The Alto III object represents an Alto III Head, you can control the
    Alto operations by instantiating a new Alto III object.
    """

    def __init__(self, ip_address: ipaddress.IPv4Address, port: int) -> None:
        super().__init__(ip_address, port)
        self.disks: [disk.Disk] = []

    @property
    def service_list(self) -> typing.List[str]:
        """
            Returns a list of Services on the ALTO III
        :return:
        """
        return self._error_check_list(self._send_tcp("get|service_list"))

    @property
    def system_name(self) -> str:
        """
        Gets the system name
        :return:
        """
        return self._error_check(self._send_tcp("get|system_name"))

    @system_name.setter
    def system_name(self, system_name: str) -> None:
        pass

    @property
    def system_serial(self) -> str:
        return self._error_check(self._send_tcp("get|system_serial"))

    @property
    def network(self) -> typing.List[str]:
        return self._error_check_list(self._send_tcp(f"get|network_address"))

    @property
    def prometheusConfig(self) -> str:
        return self._error_check(self._send_tcp(f"get|prm_file|prometheus|config"))

    @property
    def prometheusDb(self) -> str:

        res = self._send_tcp(f"get|db")

        if res.startswith("<?xml"):
            return res
        else:
            raise ValueError(f"Unexpected response format: {res}")

    def get_disk_with_free_space(self, file_size: int) -> disk.Disk:
        """
            Get a disk with enough free space to contain the given file_size in bytes
        :param file_size:
        :return:
        """
        pass

    def get_disk_by_group(self, group_name: str) -> typing.List[disk.Disk]:
        disks = self._error_check_list(self._send_tcp(f"get|disks|{group_name}"))
        return [
            disk.Disk(
                disk_uuid=uuid.UUID(d.split(":")[0]),
                ip_address=self.ip_address,
                port=self.port,
            )
            for d in disks
        ]

    def get_groups(self) -> typing.List[str]:
        """
        Get a list of groups on the alto device
        :return:
        """
        return self._error_check_list(self._send_tcp("get|groups"))

    def get_group_info(self, group_name: str) -> group.Group:
        """
        Get Information on a specific group from the alto device
        :return:
        """
        # ToDo: The group information needs to be determined and added to the Group Dataclass
        group_info = self._error_check(self._send_tcp(f"get|groupinfo|{group_name}"))
        return group.Group(name=group_name)

    def get_smart_data_by_disk_uuid(self, uuid: str) -> str:
        smart_data = self._error_check(self._send_tcp(f"get|disk_smart_data|{uuid}"))
        return smart_data
