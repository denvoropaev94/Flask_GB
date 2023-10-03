import random
import threading
import time

my_list = [random.randint(1, 100) for _ in range(1, 1000000)]

left, right = my_list[:len(my_list) // 2], my_list[len(my_list) // 2:]

my_sum = 0


def summa(list_my):
    global my_sum
    my_sum += sum(list_my)


start = time.time()
t1 = threading.Thread(target=summa, args=(left,) )
t1.start()

t2 = threading.Thread(target=summa, args=(right,) )
t2.start()

t1.join()
t2.join()

print(my_sum)
end = time.time()
print(end - start)
