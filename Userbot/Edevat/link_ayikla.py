# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from re import findall
from typing import Any

async def link_ayikla(link:str) -> Any:
    """Metindeki linkleri liste halinde return eder.."""
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url   = findall(regex, link)
    liste = [x[0] for x in url]

    if liste:
        return liste
    else:
        return None