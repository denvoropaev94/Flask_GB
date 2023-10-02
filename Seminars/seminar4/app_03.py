import asyncio
import time
import aiohttp

urls = [
    'https://www.python.org/',
    'https://en.wikipedia.org/wiki/Python',
    'https://metanit.com/python/tutorial/',
    'https://pythonworld.ru/samouchitel-python',
    'https://academy.yandex.ru/handbook/python',
    'https://www.w3schools.com/python/',
    'https://habr.com/ru/hubs/python/articles/',
    'https://www.programiz.com/python-programming',
    'https://opensource.com/resources/python',
    'https://www.vsmu.by'
]*5


async def download(url, i):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = f'site_with_url{i}.html'
            text = await response.text()

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text)
            print(url)


async def main():
    tasks = []
    for index, url in enumerate(urls):
        tasks.append(asyncio.create_task(download(url, index)))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(end_time - start_time)
    print("ITS OKEY")