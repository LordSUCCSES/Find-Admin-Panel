import requests

class color:
    RED = "\033[0;31m"
    BLUE = "\033[0;34m"
    END = "\033[0m"

class req():
    def get(self, url=""):
        try:
            sonuc = requests.get(url)
            if sonuc.status_code == 200:
                with open("bulundu.txt", "a") as file:
                    file.write(url + " | Bulundu\n")
                return url + color.BLUE + " | Admin Panel Bulundu" + color.END
            else:
                return url + color.RED + " | Bulunmadı" + color.END
        except requests.exceptions.RequestException as e:
            return url + color.RED + f" | Bağlantı Hatası: {e}\n" + color.END

url = input("URL Gir: ")
dosya_adi = "wordlist.txt"
wordlist = []

with open(dosya_adi, 'r') as dosya:
    for satir in dosya:
        kelime_dizisi = satir.strip().split()

        for kelime in kelime_dizisi:
            wordlist.append(kelime)

for kelime in wordlist:
    yeni_url = url + kelime
    print(req().get(str(yeni_url)))