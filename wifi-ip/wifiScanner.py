import subprocess

# SSID'leri taramak için bir işletim sistemi komutu çalıştırma fonksiyonu
def scan_wifi():
    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "network"])
        output = output.decode("latin-1")
        networks = output.split("\n")
        networks = networks[4:]  # İlk dört satırı atla (başlıklar)
        networks = [line.split(":")[1][1:-1] for line in networks if "SSID" in line]
        return networks
    except subprocess.CalledProcessError:
        return []

# WiFi ağlarını tarayarak sonuçları yazdırma
wifi_networks = scan_wifi()
if wifi_networks:
    print("Bulunan WiFi Ağları:")
    for network in wifi_networks:
        print(network)
else:
    print("WiFi ağı bulunamadı.")

# gizli ağları da gösteriyor ama adını yazmıyor
# import subprocess

# # SSID'leri taramak için bir işletim sistemi komutu çalıştırma fonksiyonu
# def scan_wifi():
#     try:
#         output = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=bssid"])
#         output = output.decode("latin-1")
#         networks = output.split("\n")
#         networks = networks[4:]  # İlk dört satırı atla (başlıklar)
#         networks = [line.split(":")[1][1:-1] for line in networks if "SSID" in line or "BSSID" in line]
#         return networks
#     except subprocess.CalledProcessError:
#         return []

# # WiFi ağlarını tarayarak sonuçları yazdırma
# wifi_networks = scan_wifi()
# if wifi_networks:
#     print("Bulunan WiFi Ağları:")
#     for network in wifi_networks:
#         print(network)
# else:
#     print("WiFi ağı bulunamadı.")
