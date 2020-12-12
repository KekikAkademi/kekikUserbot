# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from os import listdir

def eklentilerim():
    eklenti_listele = ""

    for dosya in listdir("./Userbot/Eklentiler/"):
        if not dosya.endswith(".py") or dosya.startswith("_"):
            continue
        eklenti_listele += f"📂 `{dosya.replace('.py','')}`\n"

    return eklenti_listele