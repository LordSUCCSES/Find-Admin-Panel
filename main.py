import requests

class req():
    def get(url = ""):
        sonuc = requests.get(url)
        if sonuc.status_code == 200:
            with open("bulundu.txt", "a") as file:
                file.write(url + " | Bulnudu\n")
            return url + " | Admin Panel Bulundu"
        else:
            return url + " | Bulunmadı"


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
    print(req.get(yeni_url))