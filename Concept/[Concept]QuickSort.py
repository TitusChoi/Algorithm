# Quick Sort

from random import randint
import time

def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    less, equal, greater = [], [], []
    for i in list:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)
    return quick_sort(less) + equal + quick_sort(greater) # recursive

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()
quick_sort(array)
end_time = time.time()

print("퀵 정렬 성능 측정:", end_time - start_time)
# 0.009939908981323242 sec