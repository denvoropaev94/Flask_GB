import threading
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


threads = []

start = time.time()

for index, url in enumerate(urls):
    t = threading.Thread(target=download_url, args=(url, index))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

end = time.time()

print(end - start)
print('Все потоки закончили!!!')
