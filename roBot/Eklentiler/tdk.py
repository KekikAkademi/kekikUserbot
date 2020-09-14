# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import requests

from roBot._edevat import logYolla

@Client.on_message(filters.command(['tdk'], ['!','.','/']) & filters.me)
async def tdk(client, message):
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
        await ilk_mesaj.edit("Arama yapabilmek için `bişeyler` girmelisiniz")
        return
    
    kelime = " ".join(girilen_yazi.split()[1:])

    if len(kelime.split()) > 1:
        mesaj = "**Lütfen tek kelime girin**"
        return

    istek = requests.get(f"http://sozluk.gov.tr/gts?ara={kelime}")

    kelime_anlamlari = istek.json()

    if "error" in kelime_anlamlari:
        mesaj = f"`{kelime}` `sozluk.gov.tr` __sitesinde bulunamadı..__"
    else:
        mesaj = f"📚 **{kelime}** __Kelimesinin Anlamları:__\n\n"
        anlamlar = kelime_anlamlari[0]["anlamlarListe"]
        for anlam in anlamlar:
            mesaj += f"👉 `{anlam['anlam']}` \n"

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")
    
    await logYolla(client, message)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "tdk",
        "aciklama"     : "sozluk.gov.tr adresinden kelime anlamı verir..",
        "parametreler" : [
            "kelime"
            ],
        "ornekler"     : [
            ".tdk kekik"
            ]
    }
})