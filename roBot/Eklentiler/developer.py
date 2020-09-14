# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Client, filters
import io, os, sys, traceback
import time, asyncio, requests

from roBot._edevat import logYolla

@Client.on_message(filters.command(["eval", "py"], ['!','.','/']) & filters.me)
async def eval(client, message):
    await logYolla(client, message)
    ilkMesaj = await message.reply_text("`İşleniyor...`")

    if message.reply_to_message:
        kod = message.reply_to_message.text
        yanitlanacakMesaj = message.reply_to_message.message_id
    else:
        kod = message.text.split(" ", maxsplit=1)[1]
        yanitlanacakMesaj = message.message_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(kod, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    cikti = ""
    if exc:
        cikti = exc
    elif stderr:
        cikti = stderr
    elif stdout:
        cikti = stdout
    else:
        cikti = "Başarılı"

    yanit = f"<b>Kod</b>: <code>{kod}</code>\n\n<b>Çıktı</b>:\n<code>{cikti.strip()}</code>\n"

    if len(yanit) > 4096:
        with open("eval.text", "w+", encoding="utf8") as cikanSonuc: cikanSonuc.write(str(yanit))
        await message.reply_document(
            document                = "eval.text",
            caption                 = kod,
            disable_notification    = True,
            reply_to_message_id     = yanitlanacakMesaj
        )
        os.remove("eval.text")
        await ilkMesaj.delete()
    else:
        await ilkMesaj.edit(yanit)
    await message.delete()

async def aexec(code, client, message):
    exec(
        f'async def __aexec(client, message): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](client, message)


@Client.on_message(filters.command(["exec", "sh"], ['!','.','/']) & filters.me)
async def execution(client, message):
    await logYolla(client, message)
    ilkMesaj = await message.reply_text("`İşleniyor...`")

    if message.reply_to_message:
        kod = message.reply_to_message.text
        yanitlanacakMesaj = message.reply_to_message.message_id
    else:
        kod = message.text.split(" ", maxsplit=1)[1]
        yanitlanacakMesaj = message.message_id

    process = await asyncio.create_subprocess_shell(
        kod,
        stdout = asyncio.subprocess.PIPE,
        stderr = asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "__Hata Yok__"
    o = stdout.decode()
    if not o:
        o = "__Çıktı Yok__"

    yanit = ""
    yanit += f"<b>Sorgu:</b>\n<u>Komut:</u>\n<code>{kod}</code>\n\n"
    yanit += f"<u>PID</u>: <code>{process.pid}</code>\n\n"
    yanit += f"<b>stderr</b>: \n<code>{e}</code>\n\n"
    yanit += f"<b>stdout</b>: \n<code>{o}</code>"

    if len(yanit) > 4096:
        with open("exec.text", "w+", encoding="utf8") as cikanSonuc: cikanSonuc.write(str(yanit))
        
        await message.reply_document(
            document                = "exec.text",
            caption                 = kod,
            disable_notification    = True,
            reply_to_message_id     = yanitlanacakMesaj
        )
        os.remove("exec.text")
        await ilkMesaj.delete()
    else:
        await ilkMesaj.edit(yanit)
    await message.delete()

@Client.on_message(filters.command(["ip"], ['!','.','/']) & filters.me)
async def public_ip(client, message):
    await logYolla(client, message)
    ip = requests.get('https://api.ipify.org').text
    await message.reply_text(f'<b>Bot IP Address:</b>\n<code>{ip}</code>', parse_mode='html')


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "py/sh/ip",
        "aciklama"     : "eski bir eklenti, kodları değerlendirilebileceği için repoda duruyor..",
        "parametreler" : [
            None
            ],
        "ornekler"     : [
            ".py | yanıtlanan python kodu",
            ".sh | yanıtlanan python kodu",
            ".ip"
            ]
    }
})