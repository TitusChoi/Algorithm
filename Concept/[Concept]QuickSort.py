# Quick Sort

from random import randint
import time

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    less, equal, greater = [], [], []
    for i in array:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)
    return quick_sort(less) + equal + quick_sort(greater) # recursive

numbers = []
for _ in range(10000):
    numbers.append(randint(1,100))

start_time = time.time()
quick_sort(numbers)
end_time = time.time()

print("퀵 정렬 성능 측정:", end_time - start_time)
# 0.012964010238647461 sec