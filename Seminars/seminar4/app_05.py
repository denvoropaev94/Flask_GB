import os
import multiprocessing
import time


def words_counter(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words_count = len(text.split())
        print(f'file:{file_path}\t - words_count: {words_count}')


if __name__ == '__main__':

    processes = []

    start = time.time()

    for root, dirs, files in os.walk('./htmls'):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            p = multiprocessing.Process(target=words_counter, args=(file_path,))
            processes.append(p)
            p.start()

    for p in processes:
        p.join()

    end = time.time()
    print(end - start)
    print('ITS OKEY')
