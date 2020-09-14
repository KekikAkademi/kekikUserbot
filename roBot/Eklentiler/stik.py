# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Client, filters
import asyncio
import random

from roBot._edevat import logYolla

@Client.on_message(filters.command("stik", ['!','.','/']) & filters.me)
async def stik(client, message):
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

    if cevaplanan_mesaj is None:
        await ilk_mesaj.edit("__stikır yapılacak mesajı yanıtlamalısın..__")
        return

    await ilk_mesaj.edit("`Stikır yapıyorum`")
    await cevaplanan_mesaj.forward("@QuotLyBot")
    
    stik_mi = False
    bar = 0
    hata_limit = 0
    
    while not stik_mi:
        try:
            msg = await client.get_history("@QuotLyBot", 1)
            kontrol = msg[0]["sticker"]["file_id"]
            stik_mi = True
        except:
            await asyncio.sleep(0.5)
            bar += random.randint(0, 10)
            try:
                await ilk_mesaj.edit(f"**Stikır**\n\n`İşleniyor %{bar}`", parse_mode="md")
                if bar >= 100:
                    pass
            except Exception as hata:
                hata_limit += 1
                if hata_limit == 3:
                    break
    
    await ilk_mesaj.edit("`Tamamlandı !`", parse_mode="md")
    msg_id = msg[0]["message_id"]
    await client.forward_messages(message.chat.id, "@QuotLyBot", msg_id)
    await client.read_history("@QuotLyBot")
    await ilk_mesaj.delete()

    await logYolla(client, message)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "stik",
        "aciklama"     : "@QuotLyBot kullanarak stikır yapar..",
        "parametreler" : [
            "yanıtlanan mesaj",
            "metin"
            ],
        "ornekler"     : [
            ".stik KekikAkademi"
            ]
    }
})