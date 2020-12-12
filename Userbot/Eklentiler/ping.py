# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Userbot.Edevat.zenginLog import log_yolla, hata_log
from Userbot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama"  : "botun hayatta olup olmadığı kontrolü..",
        "kullanim"  : [
            "mesaj",
            "yanıtlanan mesaj"
            ],
        "ornekler"  : [
            ".ping"
            ]
    }
})

from pyrogram import Client, filters
from Userbot.Edevat._pyrogram.pyro_yardimcilari import yanitlanan_mesaj
import asyncio, datetime

@Client.on_message(filters.command(['ping'], ['!','.','/']) & filters.me)
async def ping(client, message):
    # < Başlangıç
    await log_yolla(client, message)
    _ = yanitlanan_mesaj(message)
    ilk_mesaj = await message.edit("__Bekleyin..__",
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    basla = datetime.datetime.now()

    mesaj = "__Pong!__"

    bitir = datetime.datetime.now()
    sure = (bitir - basla).microseconds
    mesaj += f"\n\n**Tepki Süresi :** `{sure} ms`"

    await ilk_mesaj.edit(mesaj)

    await asyncio.sleep(3)
    await ilk_mesaj.edit("__şimdi mutlu musun?__")
    await asyncio.sleep(1)

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await hata_log(hata)
        await ilk_mesaj.edit(f'**Hata Var !**\n\n`{type(hata).__name__}`\n\n__{hata}__')

@Client.on_message(filters.command(['json'], ['!','.','/']) & filters.me)
async def jsn_ver(client, message):
    await message.edit(f"```{message.reply_to_message}```")