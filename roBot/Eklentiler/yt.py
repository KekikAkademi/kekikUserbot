# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
from pytube import YouTube
import requests, wget, os, re
from bs4 import BeautifulSoup

from roBot._edevat import logYolla

def linkAyikla(bak_buraya):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    
    url = re.findall(regex, bak_buraya)       
    
    return [x[0] for x in url] 


@Client.on_message(filters.command(['yt'], ['!','.','/']))
async def yt(client, message):
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
    if not cevaplanan_mesaj and (girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Arama yapabilmek için `Youtube Linki` girmelisiniz, veya @vid __mesajı yanıtlamalısınız..__")
        return

    if not cevaplanan_mesaj:
        verilen_link = linkAyikla(girilen_yazi)[0]
    else:
        verilen_link = linkAyikla(cevaplanan_mesaj.text)[0]

    if not cevaplanan_mesaj and (len(verilen_link.split())) > 1:
        await ilk_mesaj.edit("**Yalnızca Link Verin**")
        return

    kural = r"http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?"
    if not re.match(kural, verilen_link):
        await ilk_mesaj.edit("**Youtube Video Linki Verdiğine Emin OL!**")
        return

    vid = YouTube(verilen_link)

    istek = requests.get(verilen_link)
    baslik = BeautifulSoup(istek.content, "html.parser").title.text.split(' - YouTube')[0]
    await ilk_mesaj.edit(f"**{baslik}**\n\n\t__İndiriliyor__")
    
    video = vid.streams.get_highest_resolution().download()
    resim = wget.download(vid.thumbnail_url)
    
    await ilk_mesaj.edit(f"**{baslik}**\n\n\t__Yükleniyor__")
    await client.send_video(
        chat_id             = message.chat.id,
        video               = video,
        caption             = f"**{baslik}**",
        thumb               = resim,
        reply_to_message_id = yanitlanacak_mesaj
        )

    os.remove(video)
    os.remove(resim)

    await logYolla(client, message)
    await ilk_mesaj.delete()


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "yt",
        "aciklama"     : "Youtube'dan yüksek kaliteli video indirir..",
        "parametreler" : [
            "youtube video linki",
            "yanıtlanan mesaj"
            ],
        "ornekler"     : [
            ".yt http://www.youtube.com/watch?v=kCsq4GAZODc"
            ]
    }
})