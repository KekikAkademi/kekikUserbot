# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from os import remove
from glob import glob

async def icinden_gec(dizin):
    gecici_liste = glob(f"{dizin}/*.*")
    for dosya in gecici_liste:
        remove(dosya) 