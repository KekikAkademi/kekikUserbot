# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import requests

from roBot._edevat import logYolla

@Client.on_message(filters.command(['akaryakit'], ['!','.','/']) & filters.me)
async def akaryakit(client, message):
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

    istek = requests.get(f"https://kolektifapi.herokuapp.com/akaryakit")

    api_yaniti = istek.json()

    mesaj = "__Güncel Akaryakıt Verileri;__\n\n"
    for yanit in api_yaniti:
        mesaj += f"`{yanit['fiyati'].split(' ')[0]} ₺`\t**{yanit['turu'].split(' -- ')[0]}**\n"

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "akaryakit",
        "aciklama"     : "kolektifapi.herokuapp.com kullanarak güncel akaryakıt fiyatlarını verir..",
        "parametreler" : [
            None
            ],
        "ornekler"     : [
            ".akaryakit"
            ]
    }
})