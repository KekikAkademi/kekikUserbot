# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import asyncio
from pyrogram import Client

API_ID   = input("Telegram API ID: ")
API_HASH = input("Telegram API HASH: ")

async def session_olustur(api_id, api_hash):
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        print('\n\n')
        print(await app.export_session_string())
        print('\n')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(session_olustur(API_ID, API_HASH))