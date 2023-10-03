import random
import asyncio
import time

my_list = [random.randint(1, 100) for _ in range(1, 1000000)]

left, right = my_list[:len(my_list) // 2], my_list[len(my_list) // 2:]

my_sum = 0


async def summa(list_my):
    global my_sum
    my_sum += sum(list_my)


async def main():
    task1 = asyncio.create_task(summa(left))
    task2 = asyncio.create_task(summa(right))
    await task1
    await task2


start = time.time()
asyncio.run(main())
print(my_sum)
end = time.time()
print(end-start)
