# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#---------------#
import requests #
import json     #
#---------------#

def nobetciEczane(il,ilce):
    #response = requests.get(f'https://kekikakademi-api.herokuapp.com/nobetciEczane/{il}/{ilce}')
    response = requests.get(f'https://kekikakademi-api.herokuapp.com/nobetciEczane?il={il}&ilce={ilce}')
    data = response.text

    veri = json.loads(data) # (data, encoding='utf-8')

    print(f"\tSunucu Zamanı : {veri['istek_zamanı']}")

    for bilgi in veri['nobetciEczaneler']:
        print(f"""
    # : {bilgi['eczane_adi']}
    # : {bilgi['eczane_adresi']}
    # : {bilgi['eczane_telefonu']}
                                """)

nobetciEczane("istanbul","sultanbeyli")

def udemyKupon(ulke, hangi_sayfa):
    response = requests.get(f'https://kekikakademi-api.herokuapp.com/udemyKupon/{ulke}?Sayfa={hangi_sayfa}')
    data = response.text

    veri = json.loads(data) # (data, encoding='utf-8')

    print(f"\tSunucu Zamanı : {veri['istek_zamanı']}")

    for bilgi in veri['udemyKupon']:
        print(f"""
    # : {bilgi['kurs_adi']}
    # : {bilgi['kurs_linki']}
                                """)

udemyKupon("TR",1)
udemyKupon("EN",1)