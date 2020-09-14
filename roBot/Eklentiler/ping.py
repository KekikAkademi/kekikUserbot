# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.


from telethon import TelegramClient, errors, events, utils
import asyncio
import datetime

from roBot._edevat import logYolla

@client.on(events.NewMessage(pattern='(!|.|/)ping ?(.*)'))
async def ping(event):

    basla = datetime.datetime.now()
    
    # < Başlangıç    
    cevaplanan_mesaj    = event.reply_to_msg_id
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = event.reply_to_msg_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj
    
    ilk_mesaj = await event.edit
    (
        "__Bekleyin..__"
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
