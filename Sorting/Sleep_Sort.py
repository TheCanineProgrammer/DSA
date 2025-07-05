import threading
from random import randint
import time

l = [randint(1, 10) for _ in range(10)]
sort = []

def func(number, delay):
    time.sleep(delay)
    sort.append(number)

threads = [threading.Thread(target = func, args = (i, i)) for i in l]

for thr in threads:
    thr.start()


for j in threads:
    j.join()

print("Original List:", l)
print("Sorted List:", sort)