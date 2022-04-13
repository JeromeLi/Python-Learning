import asyncio
from aiohttp import ClientSession

tasks = []
url = "http://www.bing.com"
async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response_body = await response.read()
            print('Request URL: %s, HTTP status code: %d' % (url, response.status))
            # print(await response.text())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello(url))
    loop.close()