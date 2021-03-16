# Library Sort

from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()
array.sort()
end_time = time.time()

print("기본 정렬 라이브러리 성능 측정", end_time - start_time)
# 0.0009989738464355469 sec