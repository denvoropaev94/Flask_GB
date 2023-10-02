import argparse
import asyncio
import aiohttp
import time

site_list = [
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
]

tt_time = 0


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text_context = await response.text()
            for item in text_context:
                if 'https' in item:
                    if 'svg' in item:

                        image = item[item.find('https'):item.find('.svg') + 4]
                        try:
                            with open(str(item).split('/')[-1].replace('"', '').replace('>', '').replace("'", ''),
                                      'bw') as file:
                                time_start = time.time()
                                file.write(await session.get(image).content())
                                tt_time += (time.time() - time_start)
                                print(f"Изображение скачалось за {time.time() - time_start} секунд")
                        except:
                            continue

                    if 'png' in item:
                        image = item[item.find('https'):item.find('.png') + 4]
                        try:
                            with open(str(item).split('/')[-1].replace('"', '').replace('>', '').replace("'", ''),
                                      'bw') as file:
                                time_start = time.time()
                                file.write(await session.get(image).content())
                                tt_time += (time.time() - time_start)
                                print(f"Изображение скачалось за {time.time() - time_start} секунд")
                        except:
                            continue

                    if 'jpeg' in item:
                        image = item[item.find('https'):item.find('.jpeg') + 5]
                        try:
                            with open(str(item).split('/')[-1].replace('"', '').replace('>', '').replace("'", ''),
                                      'bw') as file:
                                time_start = time.time()
                                file.write(await session.get(image).content())
                                tt_time += (time.time() - time_start)
                                print(f"Изображение скачалось за {time.time() - time_start} секунд")
                        except:
                            continue
            print(f'Все изображения скачались за {tt_time} секунд')


async def main():
    tasks = []

    for url in site_list:
        task = asyncio.ensure_future(download([url]))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url-list', required=True)
    args_ = parser.parse_args()
    print(args_)
    processes = []
    time_start = time.time()
    site_list = [str(i) for i in args_.url_list.split(',')]
    time_start = time.time()
    asyncio.run(main())
    time_end = time.time()
    print(f'Программа завершила свою работу за {time_end - time_start} cекунд')