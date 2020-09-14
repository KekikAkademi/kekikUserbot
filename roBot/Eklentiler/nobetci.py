# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio

from roBot._edevat import logYolla

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

@Client.on_message(filters.command(['nobetci'],['!','.','/']))
async def nobetci(client, message):
    # < Başlangıç    
    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    ilk_mesaj = await message.edit("__Bekleyin..__",
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >
    
    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Arama yapabilmek için `il` ve `ilçe` girmelisiniz")
        return
    elif len(girilen_yazi.split()) == 2:
        await ilk_mesaj.edit("Arama yapabilmek için `ilçe` de girmelisiniz")
        return

    il =  " ".join(girilen_yazi.split()[1:2]).lower()   # il'i komuttan ayrıştır (birinci kelime)
    ilce = " ".join(girilen_yazi.split()[2:3]).lower()  # ilçe'yi komuttan ayrıştır (ikinci kelime)

    tr2eng = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
    il = il.translate(tr2eng)
    ilce = ilce.translate(tr2eng)
    
    mesaj = f"Aranan Nöbetçi Eczane : `{ilce}` / `{il}`\n"

    try:
        for i in nobetciEczane(il, ilce):
            mesaj += f"**\n\t⚕ {i['eczane_adi']}**\n📍 __{i['eczane_adresi']}__\n\t☎️ `{i['eczane_telefonu']}`\n\n"
    except Exception as hata:
        mesaj = f"**Uuppss:**\n\n`{hata}`"

    await logYolla(client, message)
    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "nobetci",
        "aciklama"     : "eczaneler.gen.tr'den nöbetçi eczane bilgilerini verir..",
        "parametreler" : [
            "il - ilçe"
            ],
        "ornekler"     : [
            ".nobetci çanakkale merkez"
            ]
    }
})