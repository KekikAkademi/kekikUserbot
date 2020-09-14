# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import datetime

from roBot._edevat import logYolla

@Client.on_message(filters.command(['ping'], ['!','.','/']) & filters.me)
async def ping(client, message):
    basla = datetime.datetime.now()
    
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

    mesaj = "__Pong!__"

    bitir = datetime.datetime.now()
    sure = (bitir - basla).microseconds/10000
    mesaj += f"\n\n**Tepki Süresi :** `{sure} ms`"

    await ilk_mesaj.edit(mesaj)
    
    await asyncio.sleep(3)
    await ilk_mesaj.edit("__şimdi mutlu musun?__")
    await asyncio.sleep(1)

    await logYolla(client, message)
    await ilk_mesaj.edit(mesaj)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "ping",
        "aciklama"     : "botun hayatta olup olmadığı kontrolü..",
        "parametreler" : [
            None
            ],
        "ornekler"     : [
            ".ping"
            ]
    }
})