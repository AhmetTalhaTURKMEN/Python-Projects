import nmap

print("--------------------")

def scan_network():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.1.0/24', arguments='-sn')

    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            ip_address = nm[host]['addresses']['ipv4']
            mac_address = nm[host]['addresses']['mac']
            vendor = nm[host]['vendor']
            try:
                internet_provider = nm[host]['hostnames'][0]['name']
            except KeyError:
                internet_provider = "Bilinmiyor"
            
            print("IP adresi:", ip_address)
            print("MAC adresi:", mac_address)
            print("Ağ sağlayıcısı:", vendor)
            print("İnternet sağlayıcısı:", internet_provider)
            print("--------------------")

scan_network()
