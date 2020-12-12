# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client
from pyrogram.types import Message

async def yanitlanan_mesaj(message:Message):
    yanitlanan_id = None

    if message.reply_to_message:
        yanitlanan_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        yanitlanan_id = message.message_id

    return yanitlanan_id

async def kullanici(message:Message):
    cevaplanan_mesaj = message.reply_to_message

    if cevaplanan_mesaj:
        kullanici = cevaplanan_mesaj.from_user
    else:
        kullanici = message.from_user

    kullanici_id = kullanici.id
    kullanici_adi = f"@{kullanici.username}" if kullanici.username else f"[{kullanici.first_name}](tg://user?id={kullanici_id})"

    return kullanici_adi, kullanici_id

async def kullanici_foto(client:Client, message:Message):
    cevaplanan_mesaj = message.reply_to_message

    if cevaplanan_mesaj:
        vatandas = await client.get_users(message.reply_to_message.from_user.id)
        return await client.download_media(vatandas.photo.big_file_id)

    else:
        return None