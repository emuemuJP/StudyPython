import sys
import asyncio
import random
import time

def elapsed_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - st}")
        return v
    return wrapper

class call_log():
    def __init__(self, process_description):
        self.process_description = process_description

    def __enter__(self):
        print(f"{self.process_description} start.")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"{self.process_description} end.")


async def call_web_api(url):
    with call_log("sleep:" + str(url)):
        await asyncio.sleep(random.random())
    return url

async def async_download(url):
    response = await call_web_api(url)
    return response

async def main():
    task = asyncio.gather(
        async_download('https://twitter.com/'),
        async_download('https://facebook.com/'),
        async_download('https://instagram.com/')
    )
    return await task

if sys.version_info.major ==3 and sys.version_info.minor ==6:
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(async_download('https://twitter.com/'))
else:
    result = asyncio.run(async_download('https://twitter.com/'))

print(result)

if sys.version_info.major ==3 and sys.version_info.minor ==6:
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main())
else:
    result = asyncio.run(main())

print(result)

if sys.version_info.major ==3 and sys.version_info.minor ==7:
    @elapsed_time
    async def coro(n):
        await asyncio.sleep(n)
        return n

    # 3秒で終わる
    @elapsed_time
    async def eventloop_as_task():
        task1 = asyncio.create_task(coro(1))
        task2 = asyncio.create_task(coro(2))
        task3 = asyncio.create_task(coro(3))
        print(await task1)
        print(await task2)
        print(await task3)

    result = asyncio.run(eventloop_as_task())
    
    # 6秒かかる
    @elapsed_time
    async def eventloop_as_coro():
        print(await coro(1))
        print(await coro(2))
        print(await coro(3))

    asyncio.run(eventloop_as_coro())