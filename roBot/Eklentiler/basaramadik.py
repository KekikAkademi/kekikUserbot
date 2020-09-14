# https://github.com/Quiec/AsenaUserBot

from pyrogram import Client, filters
import asyncio

from roBot._edevat import logYolla

@Client.on_message(filters.command(['basaramadik'], ['!','.','/']) & filters.me)
async def basaramadik(client, message):
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

    await ilk_mesaj.edit("Başaramadık Abi")

    animasyon = [
        "oLuM gE BurAyA QırMızi ŞortLi",
        "uLaN sEn bEnim EliMdeN tUttun İBiNe",
        "Benİ bUrdan YuQarı ÇekMedİn ULAN",
        "bEn boĞuLim ÇeQmeDin bEnİ",
        "sEnle MahMüd",
        "BAŞARAMADIK ABİ",
        "nEyi BAşaraMadıN AmınaGoyim",
        "...",
        "GüLme OğlıM ŞerEfSız",
        "**QırMızi ŞortLi SuNar**"
        ]
    
    for anime in animasyon:
        await asyncio.sleep(0.7)
        await ilk_mesaj.edit(anime)
    
    await asyncio.sleep(3)

    yarak = '...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀ ▀▀▀▀▀'

    await ilk_mesaj.edit(yarak)
    
    await ilk_mesaj.delete()


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "basaramadik",
        "aciklama"     : "Kırmızı şortli rererösü..",
        "parametreler" : [
            None
            ],
        "ornekler"     : [
            ".basaramadik"
            ]
    }
})