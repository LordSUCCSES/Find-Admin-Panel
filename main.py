import requests
from sys import exit
from time import sleep

class color:
    RED = "\033[0;31m"
    BLUE = "\033[0;34m"
    END = "\033[0m"

class req():
    def get(self, url=""):
        global bulunan
        global kalanwordlist
        try:
            sonuc = requests.get(url)
            kalanwordlist -= 1
            if sonuc.status_code == 200:
                with open("bulundu.txt", "a") as file:
                    file.write(url + " | Bulundu\n")
                    bulunan += 1
                return url + color.BLUE + f" | Admin Panel Bulundu +++++++++++++++++++  | " + color.BLUE + "Kalan Wordlist={kalanwordlist}" + color.END
            else:
                if bulunan > 0:
                    return url + color.RED + " | Bulunmadı," + color.BLUE + f" Bulunan Panel: {bulunan} | " + color.BLUE + "Kalan Wordlist={kalanwordlist}" + color.END
                else:
                    return url + color.RED + f" | Bulunmadı Kalan Wordlist={kalanwordlist}" + color.END
        except requests.exceptions.RequestException as e:
            return url + color.RED + f" | Bağlantı Hatası: {e}\n" + color.END
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
bulunan = 0

with open(dosya_adi, 'r') as dosya:
    for satir in dosya:
        kelime_dizisi = satir.strip().split()
        kalanwordlist = len(wordlist)

        for kelime in kelime_dizisi:
            wordlist.append(kelime)

for kelime in wordlist:
    yeni_url = url + kelime
    print(req().get(str(yeni_url)))