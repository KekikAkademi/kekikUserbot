# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
from pyrogram import __version__
import asyncio, json, sys
from time import time, sleep
from os import listdir

from roBot._edevat import *

def baslangic():
    surum = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}"
    konsol.print(f"\t\t\t[bold blue]@kekikUserBot[/] [yellow]:bird:[/]\t[bold red]Python: [/][i]{surum}[/]")
    basarili(f"\t\tkekikUserBot v{__version__} pyrogram tabanında çalışıyor...\n")

bilgiler = json.load(open("bilgiler.json"))

kekikUserBot        = Client(
    api_id          = bilgiler['api_id'],                   # my.telegram.org/apps
    api_hash        = bilgiler['api_hash'],                 # my.telegram.org/apps
    session_name    = f"@{bilgiler['session']}",            # Fark Etmez
    plugins         = dict(root="roBot/Eklentiler")
)

@kekikUserBot.on_message(filters.command(['start'], ['!','.','/']) & filters.me)
async def ilk(client, message):
    # Hoş Geldin Mesajı
    await message.edit("Hoş Geldin!\n/yardim alabilirsin.")            # cevapla

    await logYolla(client, message)

@kekikUserBot.on_message(filters.command(['yardim'], ['!','.','/']) & filters.me)
async def yardim_mesaji(client, message):
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
    
    basla = time()
    await ilk_mesaj.edit("__Aranıyor...__")

    mesaj = f"""Merhaba, [{message.from_user.first_name}](tg://user?id={message.from_user.id})!\n
Ben @keyiflerolsun tarafından, @KekikAkademi'de yaratıldım.\n
Kaynak kodlarım [Burada](https://github.com/KekikAkademi/kekikUserBot)
Kullanabileceğim komutlar ise eklentilerimde gizli..\n\n"""

    mesaj += """__Eklentilerimi görebilmek için__ `.eklentilist` __komutunu kullanabilirsin..__
    
`.destek` <__eklenti__> **komutuyla da eklenti hakkında bilgi alabilirsin..**
"""

    bitir = time()
    sure = bitir - basla
    mesaj += f"\n**Tepki Süresi :** `{str(sure)[:4]} sn`"

    try:
        await ilk_mesaj.edit(mesaj, disable_web_page_preview=True)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")

    await logYolla(client, message)


DESTEK_KOMUT = {}

@kekikUserBot.on_message(filters.command(['destek'], ['!','.','/']) & filters.me)
async def destek(client, message):
    """ .destek komutu için """
    
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

    girilen_yazi = message.text.split()                             # komut ile birlikle mesajı tut

    if len(girilen_yazi) == 1:                                      # eğer sadece komut varsa
        mesaj = "`DosyaAdı` **Girmelisin!**\n\n"                    # uyarı ver

        mesaj += "__Destek alınabilecek Eklentilerim;__\n"

        for dosya in listdir("./roBot/Eklentiler/"):
            if not dosya.endswith(".py"):
                continue
            mesaj += f"📂 `{dosya.replace('.py','')}`\n"
        await ilk_mesaj.edit(mesaj)
        return

    try:
        eklenti_dizini = f"./roBot/Eklentiler/{girilen_yazi[1]}.py"
        destek_json = DESTEK_KOMUT[girilen_yazi[1]]

        mesaj = f"\t⛓\t `{girilen_yazi[1]}` <u>**Eklentisi;**</u>\n"
        mesaj += f"__{destek_json['aciklama']}__\n"

        if destek_json['parametreler'][0]:
            mesaj += "\n\t✒ <u>**Kullanım;**</u>\n"
            for destek_parametre in destek_json['parametreler']:
                mesaj += f"`.{destek_json['komut']}` \t<__{destek_parametre}__>\n"

        if destek_json['ornekler'][0]:
            mesaj += f"\n\t✏ <u>**Örneğin;**</u>\n"
            for destek_ornek in destek_json['ornekler']:
                mesaj += f"`{destek_ornek}`\n"

    except KeyError:
        mesaj = f"__{girilen_yazi[1]}__\n\n\t`Böyle bir eklenti yok`"

        mesaj += "\n\n__Destek alınabilecek Eklentilerim;__\n"

        for dosya in listdir("./roBot/Eklentiler/"):
            if not dosya.endswith(".py"):
                continue
            mesaj += f"📂 `{dosya.replace('.py','')}`\n"
    
    await logYolla(client, message)
    await ilk_mesaj.edit(mesaj)

@kekikUserBot.on_message(filters.command(['logsalla'], ['!','.','/']) & filters.me)
async def logsalla(client, message):
    """ .logsalla komutu için """
    await logYolla(client, message)
    # < Başlangıç    
    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    await message.delete()
    #------------------------------------------------------------- Başlangıç >

    await message.reply_document(
        document                = f"{bilgiler['session']}.log",
        caption                 = f"__kekikUserBot__ `{message.from_user.first_name}` __logları..__",
        disable_notification    = True,
        reply_to_message_id     = yanitlanacak_mesaj
    )