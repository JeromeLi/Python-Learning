import asyncio
import aiohttp

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# Request Headers

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, verify_ssl=False) as response:
            return await response.text()

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch('https://www.uukanshu.com/b/94859/17440.html'))
loop.close
