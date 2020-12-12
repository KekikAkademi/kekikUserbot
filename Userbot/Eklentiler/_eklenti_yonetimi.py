# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Userbot.Edevat.zenginLog import log_yolla, hata_log
from Userbot import DESTEK_KOMUT

DESTEK_KOMUT.update({
    "eklenti" : {
        "aciklama"  : None,
        "kullanim"  : [
            None
            ],
        "ornekler"  : [
            ".eklentilist",
            ".eklentiver ping",
            ".eklential «Yanıtlanan Eklenti»",
            ".eklentisil !komut"
            ]
    }
})

from Userbot.Edevat._pyrogram.pyro_yardimcilari import yanitlanan_mesaj
from Userbot import SESSION_ADI
from Userbot.Edevat.eklenti_listesi import eklentilerim
from pyrogram import Client, filters
import asyncio, os

mesaj_baslangici = '`Hallediyorum..`'

@Client.on_message(filters.command(['eklentilist'], ['!','.','/']) & filters.me)
async def eklenti_list(client, message):
    await log_yolla(client, message)
    ilk_mesaj = await message.edit(mesaj_baslangici)

    mesaj = "__Eklentilerim;__\n"
    mesaj += eklentilerim()

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await hata_log(hata)
        await ilk_mesaj.edit(f'**Hata Var !**\n\n`{type(hata).__name__}`\n\n__{hata}__')

@Client.on_message(filters.command(['eklentiver'], ['!','.','/']) & filters.me)
async def eklenti_ver(client, message):
    await log_yolla(client, message)
    yanitlanacak_mesaj = yanitlanan_mesaj(message)
    ilk_mesaj = await message.edit(mesaj_baslangici)

    girilen_yazi = message.text

    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("`DosyaAdı` **Girmelisin!**")
        return

    dosya = " ".join(girilen_yazi.split()[1:2])

    if f"{dosya}.py" in os.listdir("Userbot/Eklentiler"):
        await ilk_mesaj.delete()

        await message.reply_document(
            document                = f"./Userbot/Eklentiler/{dosya}.py",
            caption                 = f"__{SESSION_ADI}__ `{dosya}` __eklentisi..__",
            disable_notification    = True,
            reply_to_message_id     = yanitlanacak_mesaj
            )

    else:
        await ilk_mesaj.edit('**Dosya Bulunamadı!**')

@Client.on_message(filters.command(['eklential'], ['!','.','/']) & filters.me)
async def eklenti_al(client, message):
    await log_yolla(client, message)
    ilk_mesaj = await message.edit("`Hallediyorum..`")
    cevaplanan_mesaj = message.reply_to_message

    if len(message.command) == 1 and cevaplanan_mesaj.document:
        if cevaplanan_mesaj.document.file_name.split(".")[-1] != "py":
            await ilk_mesaj.edit("`Yalnızca python dosyası yükleyebilirsiniz..`")
            return
        eklenti_dizini = f"./Userbot/Eklentiler/{cevaplanan_mesaj.document.file_name}"
        await ilk_mesaj.edit("`Eklenti Yükleniyor...`")

        if os.path.exists(eklenti_dizini):
            await ilk_mesaj.edit(f"`{cevaplanan_mesaj.document.file_name}` __eklentisi zaten mevcut!__")
            return

        try:
            await client.download_media(message=cevaplanan_mesaj, file_name=eklenti_dizini)
            await asyncio.sleep(2)
            await ilk_mesaj.edit(f"**Eklenti Yüklendi:** `{cevaplanan_mesaj.document.file_name}`")
            return

        except Exception as hata:
            await hata_log(hata)
            await ilk_mesaj.edit(f'**Hata Var !**\n\n`{type(hata).__name__}`\n\n__{hata}__')

    await ilk_mesaj.edit('__python betiği yanıtlamanız gerekmekte__')

@Client.on_message(filters.command(['eklentisil'], ['!','.','/']) & filters.me)
async def eklenti_sil(client, message):
    await log_yolla(client, message)
    ilk_mesaj = await message.edit(mesaj_baslangici)

    if len(message.command) == 2:
        eklenti_dizini = f"./Userbot/Eklentiler/{message.command[1]}.py"

        if os.path.exists(eklenti_dizini):
            os.remove(eklenti_dizini)
            await asyncio.sleep(2)
            await ilk_mesaj.edit(f"**Eklenti Silindi:** `{message.command[1]}`")
            return

        await ilk_mesaj.edit("`Böyle bir eklenti yok`")
        return

    await ilk_mesaj.edit("`Geçerli bir eklenti adı girin!`")