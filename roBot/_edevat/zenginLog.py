# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from roBot._edevat import logVer
import json, datetime, pytz

tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y") # Bugünün Tarihi
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")     # Bugünün Saati

bilgiler = json.load(open("bilgiler.json"))

async def logYolla(client, message):
    # < LOG Alanı
    log_dosya = f"[{saat} / {tarih}] "
    # sohbet = await client.get_chat(message.chat.id)
    
    if message.from_user.username:
        log_mesaj   = f"@{message.from_user.username}"
        log_konsol  = f"[bold red]{message.from_user.username}[/] [green]||[/] "
        log_dosya  += f"{message.from_user.username} || "
    else:
        log_mesaj   = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
        log_konsol  = f"[bold red]{message.from_user.first_name}[/] "
        log_dosya   = f"{message.from_user.first_name} "
    
    if message.chat.type != 'private' and message.chat.type != 'bot':
        log_mesaj   += f"\n\n\t\t`{sohbet.title}`__'den__ `{message.text}` __yolladı..__"
        log_konsol  += f"[yellow]{message.text}[/] [green]||[/] [bold cyan]{sohbet.title}[/] "
        log_dosya   += f"{message.text} || {sohbet.title} "
    else:
        log_mesaj   += f"\n\n\t\t`{message.text}` __yolladı..__"
        log_konsol  += f"[yellow]{message.text}[/] "
        log_dosya   += f"{message.text} "
    
    log_mesaj   +=  f"\n\n**Sohbet Türü :** __{message.chat.type}__"
    log_konsol  += f"\t[green]||[/] [magenta]{message.chat.type}[/]"
    log_dosya   += f"\t|| {message.chat.type}\n"

    # await client.send_message(bilgiler['log_id'], log_mesaj)                  # log_id'ye log gönder
    logVer(f"{log_konsol}")                                                   # zenginKonsol'a log gönder

    with open(f"{bilgiler['session']}.log", "a+") as log_yaz:                 # dosyaya log yaz
        log_yaz.write(log_dosya)
    #-------------------------------------------------------------- Log Alanı >
