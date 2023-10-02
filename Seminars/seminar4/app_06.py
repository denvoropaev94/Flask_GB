import asyncio
import os
import time
import aiofiles


async def words_counter(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        text = await file.read()
        words_count = len(text.split())
        print(f'file:{file_path}\t - words_count: {words_count}')


async def main():
    tasks = []
    for root, dirs, files in os.walk('./htmls'):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            tasks.append(asyncio.create_task(words_counter(file_path)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(end_time - start_time)
    print("ITS OKEY")
