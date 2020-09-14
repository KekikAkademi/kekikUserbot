# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Client, filters
import asyncio
from speedtest import Speedtest

from roBot._edevat import logYolla

def speed_convert(size):
    power = 2 ** 10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"

@Client.on_message(filters.command("hiz", ['!','.','/']) & filters.me)
async def hiztesti(client, message):
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
    
    await ilk_mesaj.edit("`Hız testi yapılıyor . . .`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    await ilk_mesaj.edit("**Başlama Zamanı:** "
                       f"`{result['timestamp']}`\n\n"
                       "**Download:** "
                       f"`{speed_convert(result['download'])}`\n"
                       "**Upload:** "
                       f"`{speed_convert(result['upload'])}`\n"
                       "**Ping:** "
                       f"`{result['ping']} ms`\n"
                       "**ISP:** "
                       f"`{result['client']['isp']}`")


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "hiz",
        "aciklama"     : "Botun çalıştığı sistemin internet hız testini yapar..",
        "parametreler" : [
            None
            ],
        "ornekler"     : [
            ".hiz"
            ]
    }
})