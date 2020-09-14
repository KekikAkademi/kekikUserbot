# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import requests, os, platform
from konsolTaban._evrensel import oturum, cihaz, ip
from datetime import datetime

from roBot._edevat import logYolla

@Client.on_message(filters.command(['sistem'], ['!','.','/']) & filters.me)
async def sistem(client, message):
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

    try:
        mesaj = f"__Kullanıcı :__ `{oturum}`"
        mesaj += f"\n__IP :__ `{ip}`"
        mesaj += f"\n__OS :__ `{cihaz}`"
        
        uname = platform.uname()
        mesaj += f"\n__Versiyon:__ `{uname.version}`"
        mesaj += f"\n__Makine:__ `{uname.machine}`"

        if not platform.machine() == "aarch64":
            import psutil
            boot_time_timestamp = psutil.boot_time()
            bt = datetime.fromtimestamp(boot_time_timestamp)
            boot_time_timestamp = psutil.boot_time()
            baslangicZamani = datetime.fromtimestamp(boot_time_timestamp).strftime("%d-%m-%Y | %H:%M")
            mesaj += f"\n__Boot Zamanı:__ `{bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}.{bt.second}`"
        
        await ilk_mesaj.edit(mesaj)
    
    except Exception as hata:
        await ilk_mesaj.edit(f"__başaramadık abi__\n\n\t`{hata}`")

    await logYolla(client, message)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "sistem",
        "aciklama"     : "botun çalıştığı sistemin bilgilerini verir..",
        "parametreler" : [
            None
            ],
        "ornekler"     : [
            ".sistem"
            ]
    }
})