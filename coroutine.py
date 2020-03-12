import sys
import asyncio
import random

class call_log():
    def __init__(self, process_description):
        self.process_description = process_description

    def __enter__(self):
        print(f"{self.process_description} start.")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"{self.process_description} end.")


async def call_web_api(url):
    with call_log("sleep"):
        await asyncio.sleep(random.random())
    return url

async def async_download(url):
    response = await call_web_api(url)
    return response

if sys.version_info.major ==3 and sys.version_info.minor ==6:
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(async_download('https://twitter.com/'))
else:
    result = asyncio.run(async_download('https://twitter.com/'))
print(result)