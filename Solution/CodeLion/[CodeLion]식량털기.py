# Title         : [CodeLion]식량털기.py
# Description   : Dynamic Programming

n = int(input())
array = list(map(int, input().split()))

d = [0] * 100 # 연산된 결과를 담는 테이블

# 최초의 식량 리스트 생성
d[0] = array[0]
d[1] = max(array[0], array[1]) # index 처음과 두번째 중 큰 값 선택

# 핵심 점화식 -> 노트에 적어보면서 비교해보기
for i in range(2, n): # n 전까지
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])