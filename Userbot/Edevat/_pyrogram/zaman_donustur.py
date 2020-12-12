# https://github.com/Skuzzy_xD/TelePyroBot

async def zaman_donustur(saniye: int) -> str:
    dakika, saniye  = divmod(saniye, 60)
    saat, dakika    = divmod(dakika, 60)
    gun, saat       = divmod(saat, 24)
    toparla = (
        ((str(gun) + " gün, ") if gun else "")
        + ((str(saat) + " saat, ") if saat else "")
        + ((str(dakika) + " dakika, ") if dakika else "")
        + ((str(saniye) + " saniye, ") if saniye else "")
    )
    return toparla[:-2]