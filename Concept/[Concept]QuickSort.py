# Quick Sort

from random import randint
import time

def quick_sort(list):
    pass
    return list

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()
quick_sort(array)
end_time = time.time()

print("퀵 정렬 성능 측정:", end_time - start_time)
# 4.573918104171753 sec