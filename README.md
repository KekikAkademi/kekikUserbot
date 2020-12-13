# kekikUserbot 🤖

[@KekikAkademi](https://t.me/KekikAkademi) *geliştiricileri için*, `Pyrogram` ile yazılmış, *eklenti geliştirilmeye hazır* bir **Telegram Userbot** tabanıdır.

![kekikUserBot](https://i.imgur.com/B8UWBS8.png)

- [x] *Konsol tabanı* **»** *[KekikTaban](https://github.com/keyiflerolsun/KekikTaban)*
- [x] *Userbot tabanı* **»** `Userbot/__init__.py`
- [x] *Log sistemi* **»** `Userbot/Edevat/zenginLog.py`
- [x] *Ana komutlar ve Eklenti destek sistemi* **»** `Userbot/Eklentiler/_ana_komutlar.py`
- [x] *Eklenti yönetim sistemi* **»** `Userbot/Eklentiler/_eklenti_yonetimi.py`
- [x] *Pyrogram için çeşitli* <ins>Edevatlar</ins> **»** `Userbot/Edevat/_pyrogram/`
- [x] *Örnek eklentiler* **»** `Userbot/Eklentiler/`

##

- Repo'yu _Fork Edin_ ve Cihazınıza **Kendi Reponuzu** indirin..
- Aşağıdaki `Heroku Deploy` butonuna basın.
- **String Session** oluşturun.
- _Heroku Deploy_ aşamasını tamamlayın.
- Oluşturduğunuz uygulamanın `Deploy` sekmesinden **kendi github reponuzu bağlayın** ve **otomatik deployu enable edin**
  - __kendi reponuz'da yaptığınız değişikliği push ettiğiniz anda herokuda otomatik olarak güncelleme çekilip yeniden başlar..__
- `Userbot/Eklentiler/` dizini altında yeni dosya oluşturup kendi eklentinizi geliştirmenin keyfini çıkarın..

##

# 🤖 kekikUserbot

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e84cadeb0fb347f7ba0412b47cf6a09c)](https://www.codacy.com/gh/KekikAkademi/kekikUserBot/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=KekikAkademi/kekikUserBot&amp;utm_campaign=Badge_Grade) ![Repo Boyutu](https://img.shields.io/github/repo-size/KekikAkademi/kekikUserbot) ![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/KekikAkademi/kekikUserbot&title=Profile%20Views) [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/KekikAkademi/kekikUserbot)

[Pyrogram](https://github.com/pyrogram/pyrogram) *kullanılarak oluşturulmuş* **Telegram Userbot** *geliştirme tabanı.*

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## :memo: String Session Alın

### Elle String Session Alın

```sh
git clone https://github.com/KekikAkademi/kekikUserbot.git
cd kekikUserbot
pip install -r string-requirements.txt
python3 StringSessionOlustur.py
```

### REPL RUN ile String Session Alın

[![Repl.it](https://img.shields.io/badge/REPL%20RUN-Run%20Online-blue.svg)](https://telepyrobot.skuzzyxd.repl.run/)

`String Session` **Kayıtlı Mesajlar**'*ınıza Eklenir,* **güvenliğinden [TelePyroBot](https://github.com/SkuzzyxD/TelePyroBot/) sorumludur..**

## :rocket: Deploy Edin

### HEROKU ie Deploy Edin

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/KekikAkademi/kekikUserbot)

### Elle Deploy Edin

1. Depoyu klonlayın,
2. `ayar.env` dosyasını kendinize göre düzenleyin,
3. `basla.py` betiğini çalıştırın;

```sh
git clone https://github.com/KekikAkademi/kekikUserbot.git
cd kekikUserbot
cp _ornek_ayar.env ayar.env && nano ayar.env

        # Virtualenv fetişiniz varsa kullanabilirsiniz..
        pip install virtualenv
        virtualenv -p /usr/bin/python3 venv
        . ./venv/bin/activate

# Eğer yoksa direk bu satıra atlayabilirsiniz..
pip install -r requirements.txt
python3 basla.py
```

## :green_heart: Özel Teşekkürler

* **Bir çok şey için** [By_Azade](https://github.com/muhammedfurkan) 🕊
* [TeleUserBot](https://github.com/ynsmrkrblt/TeleUserBot) **için** [ynsmrkrblt](https://github.com/ynsmrkrblt) 🕊
* [TelePyroBot](https://github.com/SkuzzyxD/TelePyroBot) **için** [SkuzzyxD](https://github.com/SkuzzyxD) 🕊
* [Nana-Remix](https://github.com/pokurt/Nana-Remix) **için** [pokurt](https://github.com/pokurt) 🕊
* [AsenaUserBot](https://github.com/Quiec/AsenaUserBot) **için** [Quiec](https://github.com/Quiec) 🕊

## :globe_with_meridians: Telif Hakkı ve Lisans

* *Copyright (C) 2020 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/KekikAkademi/kekikUserBot/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## :recycle: İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/keyiflerolsun)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*