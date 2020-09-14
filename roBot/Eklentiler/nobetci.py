# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio

from roBot._spatula.eczane import nobetciEczane

from roBot._edevat import logYolla

@Client.on_message(filters.command(['nobetci'],['!','.','/']))
async def nobetci(client, message):
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
        await ilk_mesaj.edit("Arama yapabilmek için `il` ve `ilçe` girmelisiniz")
        return
    elif len(girilen_yazi.split()) == 2:
        await ilk_mesaj.edit("Arama yapabilmek için `ilçe` de girmelisiniz")
        return

    il =  " ".join(girilen_yazi.split()[1:2]).lower()   # il'i komuttan ayrıştır (birinci kelime)
    ilce = " ".join(girilen_yazi.split()[2:3]).lower()  # ilçe'yi komuttan ayrıştır (ikinci kelime)

    tr2eng = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
    il = il.translate(tr2eng)
    ilce = ilce.translate(tr2eng)
    
    mesaj = f"Aranan Nöbetçi Eczane : `{ilce}` / `{il}`\n"

    try:
        for i in nobetciEczane(il, ilce):
            mesaj += f"**\n\t⚕ {i['eczane_adi']}**\n📍 __{i['eczane_adresi']}__\n\t☎️ `{i['eczane_telefonu']}`\n\n"
    except Exception as hata:
        mesaj = f"**Uuppss:**\n\n`{hata}`"

    await logYolla(client, message)
    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "nobetci",
        "aciklama"     : "eczaneler.gen.tr'den nöbetçi eczane bilgilerini verir..",
        "parametreler" : [
            "il - ilçe"
            ],
        "ornekler"     : [
            ".nobetci çanakkale merkez"
            ]
    }
})