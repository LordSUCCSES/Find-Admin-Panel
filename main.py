import requests
from concurrent.futures import ThreadPoolExecutor
from time import sleep

class color:
    RED = "\033[0;31m"
    BLUE = "\033[0;34m"
    END = "\033[0m"

class req():
    def __init__(self, url):
        self.url = url

    def get(self, kelime):
        try:
            sonuc = requests.get(self.url + kelime)
            if sonuc.status_code == 200:
                with open("bulundu.txt", "a") as file:
                    file.write(self.url + kelime + " | Bulundu\n")
                return self.url + kelime + color.BLUE + " | Admin Panel Bulundu +++++++++++++++++++\n" + color.END
            else:
                return self.url + kelime + color.RED + " | Bulunmadı\n" + color.END
        except requests.exceptions.RequestException as e:
            return self.url + kelime + color.RED + f" | Bağlantı Hatası: {e}\n" + color.END

def soruu():
    soru = str(input("VPN Açtınız mı? (Y/N): ")).upper()
    if soru == "Y":
        print("Devam Ediliyor.....")
        sleep(0.2)
    elif soru == "N":
        print("Kurmadan Devam Ediliyor.......")
        sleep(0.6)
    else:
        print("Lütfen Geçerli Bir Kelime Girin")
        soruu()

soruu()
url = input("URL Gir: ")
dosya_adi = "wordlist.txt"
wordlist = []

with open(dosya_adi, 'r') as dosya:
    for satir in dosya:
        kelime_dizisi = satir.strip().split()
        for kelime in kelime_dizisi:
            wordlist.append(kelime)

def thread_function(word):
    result = req(url).get(word)
    print(result)

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(thread_function, wordlist)