# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters

from roBot._edevat import logYolla

@Client.on_message(filters.command(['listadmin'],['!','.','/']) & filters.me)
async def admin(client, message):
    await logYolla(client, message)
    ilk_mesaj = await message.edit("Yönetici Listesini Çıkartıyorum..")

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":
        kurucu = ""
        adminler = ""
        
        for yonetici in await client.get_chat_members(message.chat.id, filter="administrators"):
            if not yonetici.user.is_bot:
                if yonetici.status == "creator":
                    if yonetici.user.username: kurucu += f"👑 -> @{yonetici.user.username}\n\n"
                    else: kurucu += f"👑 -> [{yonetici.user.first_name}](tg://user?id={yonetici.user.id})\n\n"
                        
                if yonetici.status == "administrator":
                    if yonetici.user.username: adminler += f" ⛑ -> @{yonetici.user.username}\n"
                    else: adminler += f" ⛑ -> [{yonetici.user.first_name}](tg://user?id={yonetici.user.id})\n"
                    
        await ilk_mesaj.edit(f'**Yönetici Listesi**:\n{kurucu}{adminler}', parse_mode="Markdown", disable_web_page_preview=True)

@Client.on_message(filters.command(['listbot'],['!','.','/']) & filters.me)
async def bot(client, message):
    await logYolla(client, message)

    ilk_mesaj = await message.edit("Bot Listesini Çıkartıyorum..")

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":
        botlar = ""

        for bot in await client.get_chat_members(message.chat.id, filter="bots"):
            botlar += f" 🤖 -> @{bot.user.username}\n"

        await ilk_mesaj.edit(f'**Bot Listesi**:\n{botlar}', parse_mode="Markdown", disable_web_page_preview=True)

@Client.on_message(filters.command(['listsilik'],['!','.','/']) & filters.me)
async def silik(client, message):
    await logYolla(client, message)
    
    ilk_mesaj = await message.edit("Silinmiş Hesapları Sayıyorum..")

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":

        sayac = 0
        for kisi in await client.get_chat_members(message.chat.id):
            if kisi.user.is_deleted:
                sayac += 1

        await ilk_mesaj.edit(f'__Silik Üye Sayısı__ : `{sayac}`', disable_web_page_preview=True)

@Client.on_message(filters.command(['listhayalet'],['!','.','/']) & filters.me)
async def hayalet(client, message):
    await logYolla(client, message)
    
    ilk_mesaj = await message.edit("Hayalet Hesapları Sayıyorum..")

    sohbetTuru = message.chat.type
    if sohbetTuru != "private":

        sayac = 0
        for kisi in await client.get_chat_members(message.chat.id):
            if kisi.user.status in ("long_time_ago", "within_month"):
                sayac += 1

        await ilk_mesaj.edit(f'__Hayalet üye sayısı__ : `{sayac}`', disable_web_page_preview=True)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "list",
        "aciklama"     : "Gruplar için listeleme eklentisi..",
        "parametreler" : [
            None
            ],
        "ornekler"     : [
            ".listadmin",
            ".listbot",
            ".listsilik",
            ".listhayalet"
            ]
    }
})