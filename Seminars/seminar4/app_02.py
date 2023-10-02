import multiprocessing
import requests
import time

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
]


def download_url(url, i):
    response = requests.get(url)
    filename = f'site_with_url{i}.html'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(url)


if __name__ == '__main__':
    proceses = []
    start = time.time()

    for index, url in enumerate(urls):
        p = multiprocessing.Process(target=download_url, args=(url, index))
        proceses.append(p)
        p.start()

    for p in proceses:
        p.join()

    end = time.time()

    print(end - start)
    print('Все потоки закончили!!!')
