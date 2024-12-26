import requests
from requests import ConnectionError


def cek_koneksi():
    try:
        inputan = input("masukkan url atau domain: ")
        url = "https://" + inputan
        response = requests.get(url)
        if response.status_code == 200:
            print(f"koneksi ke {url} berhasil, internet tersedia")
    except ConnectionError:
        print("koneksi gagal...")
    except Exception as e:
        print(f"something wrong on {e}")


cek_koneksi()
