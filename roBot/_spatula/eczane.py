# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup
import json

def nobetciEczane(il, ilce):
    url = f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.text, "lxml")
    
    eczane_adi = []
    eczane_adresi = []
    eczane_telefonu = []

    for tablo in corba.find('div', id='nav-bugun'):
        for ad in tablo.findAll('span', class_='isim'):
            eczane_adi.append(ad.text)

        for adres in tablo.findAll('span', class_='text-capitalize'):
            eczane_adresi.append(adres.text)

        for telefon in tablo.findAll('div', class_='col-lg-3 py-lg-2'):
            eczane_telefonu.append(telefon.text)
        
    liste = []
    for adet in range(0, len(eczane_adi)):
        sozluk = {}
        sozluk['eczane_adi'] = eczane_adi[adet]
        sozluk['eczane_adresi'] = eczane_adresi[adet]
        sozluk['eczane_telefonu'] = eczane_telefonu[adet]
        liste.append(sozluk)

    return liste

jsonGorsel = lambda il, ilce: json.dumps(nobetciEczane(il, ilce), indent=2, sort_keys=True, ensure_ascii=False)
# print(jsonGorsel("canakkale", "merkez"))

basliklar = lambda il, ilce: [anahtar for anahtar in nobetciEczane(il, ilce)[0].keys()]
# print(basliklar('canakkale', 'merkez'))