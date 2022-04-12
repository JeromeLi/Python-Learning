import time
import asyncio

# define a coroutine
async def hello():
    await asyncio.sleep(1)
    print('Hello World! : %s' % time.ctime() )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [hello() for i in range(5)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()