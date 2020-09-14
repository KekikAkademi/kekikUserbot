# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import requests

from roBot._edevat import logYolla

@Client.on_message(filters.command(['sondakika'], ['!','.','/']) & filters.me)
async def sonDakika(client, message):
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

    istek = requests.get(f"https://kolektifapi.herokuapp.com/haber")

    api_yaniti = istek.json()

    mesaj = "📰 __NTV Kaynağından Son Dakika Haberleri;__\n\n"
    say = 0
    for yanit in api_yaniti:
        mesaj += f"🗞️ **[{yanit['Haber']}]({yanit['Link']})**\n\n"
        say += 1
        if say == 5:
            break

    try:
        await ilk_mesaj.edit(mesaj, disable_web_page_preview=True)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")
    
    await logYolla(client, message)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "sondakika",
        "aciklama"     : "kolektifapi.herokuapp.com kullanarak NTV son dakika haberlerini verir..",
        "parametreler" : [
            None
            ],
        "ornekler"     : [
            ".sondakika"
            ]
    }
})