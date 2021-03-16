# Selection Sort

from random import randint
import time

def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
    
        list[i], list[min_index] = list[min_index], list[i]
    return list

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()
selection_sort(array)
end_time = time.time()

print("선택 정렬 성능 측정:", end_time - start_time)
# 4.573918104171753 sec