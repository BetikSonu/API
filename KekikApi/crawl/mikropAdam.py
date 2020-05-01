# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#-------------------------------#
import requests, re             #
from bs4 import BeautifulSoup   #
#-------------------------------#

def mikropAdam():
    link = f"https://mikropadam.com/sitemap.xml"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(link, headers=kimlik)
    soup = BeautifulSoup(istek.text, "html5lib")

    #------------------------------------------------------#
    #print(istek)              # <Response [200]>
    #print(soup)               # Kaynak Kodlar
    #print(soup.title.text)    # Kaynak Kodu Sayfa Başlığı
    #------------------------------------------------------#

    liste = []

    for gelenlink in soup.findAll('loc'):
        if gelenlink.text.endswith(".html"):
            mikropGez = requests.get(gelenlink.text, headers=kimlik)
            mikropSoup = BeautifulSoup(mikropGez.text, "html5lib")

            #print(mikropSoup.title.text) # ♥

            for download in mikropSoup.findAll('a', attrs={'href': re.compile("^https://storage.cloud.google.com")}):
                sozluk = {}
                sozluk['dosya_adi'] = mikropSoup.title.text.replace(" » Mikrop Tadında Paylaşımlar  Bir Mikroptan Daha Fazlası :D","")
                sozluk['dosya_linki'] = download['href']
                liste.append(sozluk)

    return liste

#mikropAdam()