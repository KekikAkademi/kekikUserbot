# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
from time import time
import requests

from roBot import logYolla

@Client.on_message(filters.command(['gg'], ['!','.', '/']) & filters.me)
async def googleNasilKullanilir(client, message):                           # fonksiyon oluşturuyoruz
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
        await ilk_mesaj.edit("Arama yapabilmek için kelime girmelisiniz..")
        return
    await ilk_mesaj.edit("Aranıyor...")
    
    basla = time()                                                          # Zamanı Başlat
    girdi = " ".join(girilen_yazi.split()[1:])                              # girdiyi komuttan ayrıştır

    mesaj = f"Aranan Kelime : `{girdi}`\n\n"                                # Mesaj'ı Başlatıyoruz

    ara = girdi.replace(" ", "+")                                           # boşlukları + ya çeviriyoruz
    numune = f"https://da.gd/s?url=https://lmgtfy.com/?q={ara}%26iie=1"     # nasilgooglekullanilir linkimize ekliyoruz
    api_tepki = requests.get(numune).text                                   # api tepkisini alıyoruz

    if api_tepki:                                                           # eğer tepki varsa
        mesaj += f"🔍 [{girdi}]({api_tepki.rstrip()})"                      # Mesaja Ekle
        bitir = time()                                                      # Zamanı Durdur
        sure = bitir - basla                                                # Duran - Başlayan Zaman
        mesaj += f"\n\nTepki Süresi : `{str(sure)[:4]} sn`"                 # Mesaja Ekle
        try:                                                                # Dene
            await ilk_mesaj.edit(mesaj)
        except Exception as hata:
            await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")
    else:                                                                   # Eğer tepki yoksa
        await ilk_mesaj.edit("Hatalı bişeyler var, daha sonra tekrar deneyin..") # uyarı ver
    
    await logYolla(client, message)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "gg",
        "aciklama"     : "goygoy google linki verir..",
        "parametreler" : [
            "herhangi bişi"
            ],
        "ornekler"     : [
            ".gg python nedir"
            ]
    }
})