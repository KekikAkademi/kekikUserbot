from pyrogram import Client, filters
from pyrogram.types import Message
from requests import post
import shutil, os
import asyncio
import urllib

from roBot._edevat import logYolla

@Client.on_message(filters.command(['carbon'], ['!','.','/']) & filters.me)
async def carbon_api(client, message):
    await logYolla(client, message)
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

    json = {
        "backgroundColor": "rgba(31, 129, 109, 1)",
        "theme": "monokai",
        "exportSize": "4x",
        "language": "auto"
    }

    # 'https://carbon.now.sh/?t={theme}&l={lang}&code={code}&bg={bg}'

    girilen_yazi = message.text
    if not cevaplanan_mesaj and (girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("__Carbon'a yönlendirebilmem için bişeyler verin ya da mesaj yanıtlayın..__")
        return

    if not cevaplanan_mesaj:
        json['code'] = urllib.parse.quote(girilen_yazi.split(" ", 1)[1])
    
    elif cevaplanan_mesaj and cevaplanan_mesaj.document:
        gelen_dosya = await cevaplanan_mesaj.download()
        
        veri_listesi = None
        with open(gelen_dosya, "rb") as oku:
            veri_listesi = oku.readlines()
        
        inen_veri = ""
        for veri in veri_listesi:
            inen_veri += veri.decode("UTF-8")
        
        json['code'] = urllib.parse.quote(inen_veri)

        os.remove(gelen_dosya)
    
    elif cevaplanan_mesaj.text:
        json['code'] = urllib.parse.quote(cevaplanan_mesaj.text)
    else:
        await ilk_mesaj.edit("__güldük__")
        return
    

    await ilk_mesaj.edit('`Carbon yapılıyor..`')


    apiUrl = "http://carbonnowsh.herokuapp.com"
    istek = post(apiUrl, json=json, stream=True)
    carbon_gorsel = "carbon.png"
    
    if istek.status_code == 200:
        istek.raw.decode_content = True
        
        with open(carbon_gorsel, "wb") as carbon_yazdir:
            shutil.copyfileobj(istek.raw, carbon_yazdir)
        
        await client.send_photo(
            message.chat.id,
            carbon_gorsel,
            caption             =   "__kekikUserBot tarafından dönüştürülmüştür__",
            reply_to_message_id =   yanitlanacak_mesaj,
        )
        await ilk_mesaj.delete()
    else:
        await ilk_mesaj.edit("**Görsel Alınamadı..**")

    os.remove(carbon_gorsel)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "carbon",
        "aciklama"     : "carbon.now.sh api..",
        "parametreler" : [
            "Yanıtlanan Mesaj",
            "Yanıtlanan Dosya",
            "Metin"
            ],
        "ornekler"     : [
            None
            ]
    }
})