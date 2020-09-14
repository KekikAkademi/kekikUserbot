# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import requests
from bs4 import BeautifulSoup
import wikipediaapi

from roBot._edevat import logYolla

def yerliNedir(kelime):
    kelime = kelime.title()

    url     = f"https://www.nedir.com/{kelime}"
    kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek   = requests.get(url, kimlik)
    corba   = BeautifulSoup(istek.text, "lxml")

    if corba.select('#content > article > p:nth-child(3)'):
        ilk_paragraf = corba.select('#content > article > p:nth-child(3)')
        
        try:
            ikinci_paragraf = corba.select('#content > article > p:nth-child(4)')
            metin = f"__{ilk_paragraf[0].text}__\n\n__{ikinci_paragraf[0].text}__"
        except:
            metin = f"__{ilk_paragraf[0].text}__"
        
        return f"**{kelime}**\n\n{metin}"
    
    elif corba.select('#didyoumean'):
        metin = googleAsor(kelime)
        
        bunu_mu_demek_istediniz = corba.select('#didyoumean')[0].text
        soru, oneri = bunu_mu_demek_istediniz.split(':')
        
        metin += f"\n\n**veya {soru.lower()}**:"
        for oner in oneri.split(','):
            metin += f"`{oner}`, "

        return metin
    
    else:
        return nedirViki(kelime)

def nedirViki(kelime):
    kelime = kelime.title()

    viki = wikipediaapi.Wikipedia('tr')

    liste = viki.page(kelime).text.split('\n')

    if len(liste[0]) > 5:
        try:
            metin = f"__{liste[0]}__\n\n__{liste[1]}__"
        except:
            metin = f"__{liste[0]}__"
        
        return f"**{kelime}** `Vikipedi`:\n\n{metin}"
    else:
        return googleAsor(kelime)

def googleAsor(kelime):
    kelime = kelime.title()

    url     = f"https://www.google.com/search?&q={kelime} nedir? 'wiki'" + "&lr=lang_tr&hl=tr"
    kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek   = requests.get(url, kimlik)
    corba   = BeautifulSoup(istek.text, "lxml")

    nedir = corba.find('div', class_='BNeawe').text
    
    if nedir.endswith(' - Vikipedi'):
        return nedirViki(nedir.split(' - ')[0])

    return f"**{kelime}**\n\n__{nedir}__"

# print(yerliNedir("Pablo Escobar"))

@Client.on_message(filters.command(['nedir'],['!','.','/']) & filters.me)
async def nedir(client, message):
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
        await ilk_mesaj.edit("Arama yapabilmek için `bişeyler` girmelisiniz")
        return
    
    sorulan_soru = " ".join(girilen_yazi.split()[1:])

    try:
        mesaj = yerliNedir(sorulan_soru)
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
        "komut"        : "nedir",
        "aciklama"     : "sırasıyla nedir.com, wikipedia ve google araması yapar..",
        "parametreler" : [
            "herhangi bişi"
            ],
        "ornekler"     : [
            ".nedir Pablo Escobar"
            ]
    }
})