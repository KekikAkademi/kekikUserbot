# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import os, platform, requests, datetime, pytz

from kekikTaban._renkler import *
from kekikTaban._evrensel import *

#---------------------------------------------------------------#
try:
    kullanici_adi = os.getlogin()                                     # Kullanıcı Adı
except:
    import pwd
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]                     # Kullanıcı Adı

bilgisayar_adi = platform.node()                                      # Bilgisayar Adı
oturum = kullanici_adi + "@" + bilgisayar_adi                         # Örn.: "kekik@Administrator"

isletim_sistemi = platform.system()                                        # İşletim Sistemi
bellenim_surumu = platform.release()                                       # Sistem Bellenim Sürümü
cihaz = isletim_sistemi + " | " + bellenim_surumu                          # Örn.: "Windows | 10"

tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y") # Bugünün Tarihi
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")     # Bugünün Saati
zaman = tarih + " | " + saat

ip_req = requests.get('http://ip.42.pl/raw')    # Harici IP'yi bulmak için bir GET isteği yolluyoruz
ip = ip_req.text                                # ip Adresi

ust_bilgi = f"\t\t\t{l_siyah}{kullanici_adi} {l_yesil}({ip})\n"
ust_bilgi += f"\t\t\t  {l_kirmizi}{cihaz}\n"
ust_bilgi += f"\t\t\t   {sari}{zaman}\n"
#-----------------------------------------------#

#---------------------------------------#
def temizle():                          # Temizle adında bir fonksiyon oluşturduk
    if isletim_sistemi == "Windows":    # Eğer İşletim Sistemi "Windows" ise
        os.system("cls")                # Sisteme "cls" komutu gönder
    else:                               # Sistem Windows değil ise
        os.system("clear")              # Sisteme "clear" komutu gönder
temizle()                               # Temizle fonksiyonumuzu çağırdık
#---------------------------------------#