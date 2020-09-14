# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
from os import remove
import requests
from bs4 import BeautifulSoup

from roBot._edevat import logYolla

def havaDurumu(sehir):
    url = f"https://www.google.com/search?&q={sehir} hava durumu" + "&lr=lang_tr&hl=tr"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.text, "lxml")

    gun_durum = corba.findAll('div', class_='BNeawe')
    gun, durum = gun_durum[3].text.strip().split('\n')
    derece = corba.find('div', class_='BNeawe').text

    return f"**{sehir.capitalize()}**\n\t__{gun}__\n\t\t`{durum} {derece}`"

# print(havaDurumu("mumbai"))
# print(havaDurumu("bahreyn"))
# print(havaDurumu("brüksel"))
# print(havaDurumu("çanakkale"))
# print(havaDurumu("new york"))

@Client.on_message(filters.command(['hava'],['!','.','/']) & filters.me)
async def hava(client, message):
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
        await ilk_mesaj.edit("Arama yapabilmek için `şehir` girmelisiniz")
        return
    
    sehir = " ".join(girilen_yazi.split()[1:2])

    try:
        mesaj = havaDurumu(sehir)
    except Exception as hata:
        mesaj = f"**Uuppss:**\n\n`{hata}`"

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")
    
    await logYolla(client, message)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "hava",
        "aciklama"     : "google'dan hava durumu bilgilerini verir..",
        "parametreler" : [
            "yer adı"
            ],
        "ornekler"     : [
            ".hava çanakkale merkez"
            ]
    }
})