# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Userbot.Edevat.zenginLog import log_yolla, hata_log
from Userbot import DESTEK_KOMUT, API_ID, API_HASH, STRING_SESSION, SESSION_ADI
from Userbot.Edevat.eklenti_listesi import eklentilerim
from Userbot.Edevat._pyrogram.pyro_yardimcilari import yanitlanan_mesaj, kullanici
from Userbot.Edevat.deldog import deldog

from pyrogram import Client, filters
from pyrogram.types import Message
from time import time

mesaj_baslangici = '`Hallediyorum..`'

@Client.on_message(filters.command(['yardim'], ['!','.','/']) & filters.me)
async def yardim_mesaji(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    ilk_mesaj = await message.edit(mesaj_baslangici, disable_web_page_preview = True)
    #------------------------------------------------------------- Başlangıç >

    basla = time()
    await ilk_mesaj.edit("__Aranıyor...__")

    mesaj = f"""Merhaba, [{message.from_user.first_name}](tg://user?id={message.from_user.id})!\n
Ben @keyiflerolsun tarafından, @KekikAkademi'de yaratıldım.\n
Kaynak kodlarım [Burada](https://github.com/KekikAkademi/kekikUserbot)
Kullanabileceğim komutlar ise eklentilerimde gizli..\n\n"""

    mesaj += """__Eklentilerimi görebilmek için__ `.eklentilist` __komutunu kullanabilirsin..__

`.destek` «__eklenti__» **komutuyla da eklenti hakkında bilgi alabilirsin..**
"""

    bitir = time()
    sure = bitir - basla
    mesaj += f"\n**Tepki Süresi :** `{sure * 1000:.3f} ms`"

    try:
        await ilk_mesaj.edit(mesaj, disable_web_page_preview=True)
    except Exception as hata:
        await hata_log(hata, ilk_mesaj)

@Client.on_message(filters.command(['destek'], ['!','.','/']) & filters.me)
async def destek(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    ilk_mesaj = await message.edit(mesaj_baslangici, disable_web_page_preview = True)
    #------------------------------------------------------------- Başlangıç >

    girilen_yazi = message.text.split()

    if len(girilen_yazi) == 1:
        mesaj = "`DosyaAdı` **Girmelisin!**\n\n"

        mesaj += "__Destek alınabilecek Eklentilerim;__\n"
        mesaj += eklentilerim()

        await ilk_mesaj.edit(mesaj)
        return

    try:
        destek_json = DESTEK_KOMUT[girilen_yazi[1]]
        mesaj = f"\t📝\t `{girilen_yazi[1]}` <u>**Eklentisi;**</u>\n"

        if destek_json['aciklama']:
            mesaj += f"__{destek_json['aciklama']}__\n"

        if destek_json['kullanim'][0]:
            mesaj += "\n\t✒️ <u>**Kullanım;**</u>\n"
            for destek_parametre in destek_json['kullanim']:
                mesaj += f"\t«<i>{destek_parametre}</i>»\n"

        if destek_json['ornekler'][0]:
            mesaj += "\n\t✏️ <u>**Örneğin;**</u>\n"
            for destek_ornek in destek_json['ornekler']:
                mesaj += f"```{destek_ornek}```\n"

    except KeyError:
        mesaj = f"`{girilen_yazi[1]}`\n\t**Adında bir eklenti bulunamadı..**"

        mesaj += "\n\n__Destek alınabilecek Eklentilerim;__\n"
        mesaj += eklentilerim()

    await ilk_mesaj.edit(mesaj)

@Client.on_message(filters.command(['logsalla'], ['!','.','/']) & filters.me)
async def logsalla(client:Client, message:Message):
    await log_yolla(client, message)
    yanit_id = await yanitlanan_mesaj(message)

    with open(f"@{SESSION_ADI}.log", "r") as dosya_log:
        raw_log = await deldog(dosya_log.read())

    await message.reply(
        f"**Log istersin de vermez miyim..**\n\n__[@{SESSION_ADI} Logları]({raw_log})__",
        disable_web_page_preview    = True,
        reply_to_message_id         = yanit_id
    )

@Client.on_message(filters.command(['envsalla'], ['!','.','/']) & filters.me)
async def envsalla(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    ilk_mesaj = await message.edit(mesaj_baslangici, disable_web_page_preview = True)
    #------------------------------------------------------------- Başlangıç >

    kullanici_adi, kullanici_id = await kullanici(message)

    env_bilgileri = f"""__İşte {kullanici_adi} » {SESSION_ADI} Bilgileri;__

**API_ID :**
`{API_ID}`

**API_HASH :**
`{API_HASH}`

**STRING_SESSION :**
`{STRING_SESSION}`

**KİMSEYLE PAYLAŞMAYINIZ!!**

`Sağlayıcı :` **@KekikAkademi**"""

    await client.send_message(kullanici_id, env_bilgileri)

    await ilk_mesaj.edit(f"**{kullanici_adi} !**\n\n`ayar.env` **için gerekli olan bilgilerini kaydettim..**\n\n__Kayıtlı Mesajlarına Bakabilirsin..__")