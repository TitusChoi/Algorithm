# Title         : [CodeLion]InsertionSort.py
# Description   : insertion sorting -> 실전용

from random import randint
import time

numbers = []
for _ in range(10000):
    numbers.append(randint(1,100))

def insertion_sort(array):
    n = len(array) # len 함수도 for문이므로 시간복잡도 해결을 위해 제거
    
    if n <= 1:
        return array
    for i in range(1, n): # 2행부터 시작
        for j in range(i, 0, -1): # 거꾸로 값 확인하기 i부터 1까지
            if array[j] < array[j - 1]: # 작으면 바꾸기
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array

start_time = time.time()
insertion_sort(numbers)
end_time = time.time()

print("삽입 정렬 라이브러리 성능 측정", end_time - start_time)
# 4.514954328536987 sec