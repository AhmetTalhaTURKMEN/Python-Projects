import subprocess

# SSID'leri taramak için bir işletim sistemi komutu çalıştırma fonksiyonu
def scan_wifi():
    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=bssid"])
        output = output.decode("latin-1")
        networks = output.split("\n")
        networks = networks[4:]  # İlk dört satırı atla (başlıklar)
        wifi_networks = []
        for line in networks:
            if "SSID" in line:
                ssid = line.split(":")[1][1:-1]
            elif "Signal" in line:
                signal_power = line.split(":")[1][1:-1]
                wifi_networks.append((ssid, signal_power))
        return wifi_networks
    except subprocess.CalledProcessError:
        return []

# WiFi ağlarını tarayarak sonuçları yazdırma
wifi_networks = scan_wifi()
if wifi_networks:
    print("Bulunan WiFi Ağları:")
    for network in wifi_networks:
        ssid, signal_power = network
        print("SSID: {}, Signal Power: {}".format(ssid, signal_power))
else:
    print("WiFi ağı bulunamadı.")
