# Selection Sort

from random import randint
import time

def selection_sort(array):
    if len(array) <= 1:
        return array
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
    
        array[i], array[min_index] = array[min_index], array[i]
    return array

numbers = []
for _ in range(10000):
    numbers.append(randint(1,100))

start_time = time.time()
selection_sort(numbers)
end_time = time.time()

print("선택 정렬 성능 측정:", end_time - start_time)
# 4.573918104171753 sec