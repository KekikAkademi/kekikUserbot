# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
from time import time
from google_search_client.search_client import GoogleSearchClient
import ast

from roBot._edevat import logYolla

@Client.on_message(filters.command(['google'], ['!','.','/']) & filters.me)
async def google(client, message):
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
    
    basla = time()
    girdi = " ".join(girilen_yazi.split()[1:])
    mesaj = f"Aranan Kelime : `{girdi}`\n\n"
    
    istek = GoogleSearchClient()
    sonuclar = istek.search(girdi).to_json()
    
    if sonuclar:
        i = 1
        for sonuc in ast.literal_eval(sonuclar):
            mesaj += f"🔍 [{sonuc['title']}]({sonuc['url']})\n"
            i += 1
            if i == 5:
                break
        
        bitir = time()
        sure = bitir - basla
        mesaj += f"\nTepki Süresi : `{str(sure)[:4]} sn`"
        
        try:
            await ilk_mesaj.edit(mesaj, disable_web_page_preview    = True,)
        except Exception as hata:
            await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")
    else:                                                                           # Eğer tepki yoksa
        await ilk_mesaj.edit("Hatalı bişeyler var, daha sonra tekrar deneyin..")    # uyarı ver
    
    await logYolla(client, message)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "google",
        "aciklama"     : "google araması yapar..",
        "parametreler" : [
            "herhangi bişi"
            ],
        "ornekler"     : [
            ".google KekikAkademi"
            ]
    }
})