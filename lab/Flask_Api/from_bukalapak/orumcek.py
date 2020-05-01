#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#-------------------------------#
from bs4 import BeautifulSoup   #
import requests                 #
#-------------------------------#

def Scraping():
    liste = []
    for sayfa in range(0, 3):
        sayfa = sayfa + 1
        base_url = 'https://www.bukalapak.com/promo/kebutuhan-harian-kesehatan?g=2&from=current-day-promo-old-1&page=' + str(sayfa)
        # print(base_url)

        # Request URL and Beautiful Parser
        r = requests.get(base_url)
        soup = BeautifulSoup(r.text, "html.parser")

        urunler = soup.find_all('div', class_="product-card")
        # print(len(urunler))

        for item in urunler:
            sozluk = { }

            # image
            urun_resmi = item.find("img", {"class":"product-media__img"})
            # image = image.text.replace('\n', "").strip()
            urun_resmi = urun_resmi['src']
            sozluk['urun_resmi'] = urun_resmi

            # name & link
            urun_adi = item.find("a", {"class":"product__name"})
            urun_link = 'https://www.bukalapak.com' + str(urun_adi.get('href'))
            urun_adi = urun_adi.text.replace('\n', "").strip()
            sozluk['urun_link'] = urun_link
            sozluk['urun_adi'] = urun_adi

            # price
            urun_fiyati = item.find("span", {"class":"amount"})
            urun_fiyati = urun_fiyati.text.replace('\n', "").strip()
            sozluk['urun_fiyati'] = 'Rp' + urun_fiyati

            liste.append(sozluk)
    return liste

#---------------------------#
if __name__ == "__main__":  #
    print(Scraping())       #
#---------------------------#