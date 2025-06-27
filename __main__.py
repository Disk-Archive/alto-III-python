################################################
######### Example for Testing Purpose ##########
################################################

from alto import AltoIII
import ipaddress

ip = ipaddress.IPv4Address("192.168.39.95")
port = 6480


def main():

    try:
        alto = AltoIII(ip, port)
        print("System Name:", alto.system_name)
        print(alto.network)
        print(alto.prometheusConfig)
        print(alto.prometheusDb)
        print(alto.get_smart_data_by_disk_uuid("66eca1d7-d785-45e6-8945-fb2a6e318a78"))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
