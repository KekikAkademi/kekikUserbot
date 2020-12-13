# https://github.com/pokurt/Nana-Remix

import aiohttp

async def deldog(veri) -> str:
    baslangic_url = 'https://nekobin.com'

    async with aiohttp.ClientSession() as oturum:
        async with oturum.post(f'{baslangic_url}/api/documents', json={"content":veri}, timeout=3) as yanit:
            url = (await yanit.json())["result"]["key"]
            return f'{baslangic_url}/raw/{url}'