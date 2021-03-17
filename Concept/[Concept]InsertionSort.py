# Title         : [Concept]InsertionSort.py
# Description   : insertion sorting

from random import randint
import time

numbers = []
for _ in range(10000):
    numbers.append(randint(1,100))

def insertion_sort(array):
    if len(array) <= 1:
        return array
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key: # key랑 같아질 경우 끝냄!
            array[j + 1] = array[j] # 오른쪽으로 한 칸 밀기
            j -= 1
        array[j + 1] = key # 비어있는 왼쪽 칸에 key 값 넣기 빼줘서 그렇지 array[j]랑 같음
    return array

start_time = time.time()
insertion_sort(numbers)
end_time = time.time()

print("삽입 정렬 라이브러리 성능 측정", end_time - start_time)
# 4.514954328536987 sec