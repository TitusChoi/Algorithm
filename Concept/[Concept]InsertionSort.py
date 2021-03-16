# Concept : Insertion Sort
from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1,100))

def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        key = list[i]
        while j >= 0 and list[j] > key: # key랑 같아질 경우 끝냄!
            list[j + 1] = list[j] # 오른쪽으로 한 칸 밀기
            j -= 1
        list[j + 1] = key # 비어있는 왼쪽 칸에 key 값 넣기 빼줘서 그렇지 list[j]랑 같음
    return list

start_time = time.time()
insertion_sort(array)
end_time = time.time()

print("삽입 정렬 라이브러리 성능 측정", end_time - start_time)
# 4.514954328536987 sec