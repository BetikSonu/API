#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#-----------------------#
import requests         #
from time import sleep  #
#-----------------------#
from threading import Thread


def TR(sayfa):
    try:
        while True:
            response = requests.get(f'http://127.0.0.1:5000/udemyKupon/TR?Sayfa={sayfa}')
            data = response.text

            json_yaz = open("TR.json", "w+")
            json_yaz.write(data)
            json_yaz.close()

            sleep(60*60)        # 1 saat sleep
    except requests.exceptions.ConnectionError:
        print('\t/TR/ | Api Bağlantısı Sağlanamadı!')

def EN(sayfa):
    try:
        while True:
            response = requests.get(f'http://127.0.0.1:5000/udemyKupon/EN?Sayfa={sayfa}')
            data = response.text

            json_yaz = open("EN.json", "w+")
            json_yaz.write(data)
            json_yaz.close()

            sleep(60*60)        # 1 saat sleep
    except requests.exceptions.ConnectionError:
        print('\t/EN/ | Api Bağlantısı Sağlanamadı!')

trJson = Thread(target=TR, args=("1"))
enJson = Thread(target=EN, args=("1"))
