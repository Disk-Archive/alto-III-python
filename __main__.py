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

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
