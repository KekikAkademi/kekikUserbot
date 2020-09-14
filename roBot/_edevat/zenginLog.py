# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
import telethon
from telethon import events, client
from telethon.tl.functions.users import GetFullUserRequest
# from pyrogram import Client
# from pyrogram.types import Message
from roBot._edevat import logVer
import json
from kekikTaban._evrensel import saat, tarih

bilgiler = json.load(open("bilgiler.json"))

async def logYolla(event) -> bool:
    # < LOG Alanı
    log_dosya = f"[{saat} / {tarih}] "
    sohbet = await event.client(GetFullUserRequest(event.from_id))
    chat = await event.client.get_chat()
    
    if sohbet.username:
        log_mesaj   = f"@{sohbet.username}"
        log_konsol  = f"[bold red]{sohbet.username}[/] [green]||[/] "
        log_dosya  += f"{sohbet.username} || "
    else:
        log_mesaj   = f"[{sohbet.first_name}](tg://user?id={sohbet.id})"
        log_konsol  = f"[bold red]{sohbet.first_name}[/] "
        log_dosya   = f"{sohbet.first_name} "
    
    if event.is_group != True and event.is_bot != True:
        log_mesaj   += f"\n\n\t\t`{chat.title}`__'den__ `{event.message.message}` __yolladı..__"
        log_konsol  += f"[yellow]{event.message.message}[/] [green]||[/] [bold cyan]{chat.title}[/] "
        log_dosya   += f"{event.message.message} || {chat.title} "
    else:
        log_mesaj   += f"\n\n\t\t`{event.message.message}` __yolladı..__"
        log_konsol  += f"[yellow]{event.message.message}[/] "
        log_dosya   += f"{event.message.message} "
    
#     log_mesaj   +=  f"\n\n**Sohbet Türü :** __{message.chat.type}__"
#     log_konsol  += f"\t[green]||[/] [magenta]{message.chat.type}[/]"
#     log_dosya   += f"\t|| {message.chat.type}\n"

    # await client.send_message(bilgiler['log_id'], log_mesaj)                  # log_id'ye log gönder
    logVer(f"{log_konsol}")                                                   # zenginKonsol'a log gönder

    with open(f"{bilgiler['session']}.log", "a+") as log_yaz:                 # dosyaya log yaz
        log_yaz.write(log_dosya)
    #-------------------------------------------------------------- Log Alanı >
