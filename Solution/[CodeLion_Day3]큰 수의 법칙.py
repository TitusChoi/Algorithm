# Title         : [CodeLion_Day3]큰 수의 법칙.py
# Description   : greedy

# 손 풀기 문제
# n, m = map(int, input().split())
# print(('*' * n + '\n') * m)

# 큰 수의 법칙
n, m, k = map(int, input().split())

# n개의 값
data = list(map(int, input().split()))
data.sort()

first = data[-1]
second = data[-2]

result = 0

'''
while True:
    for i in range(k):  # 가장 큰 수 k 번 더하기
        if m == 0:      # m = 0일 때 for문 탈출
            break
        result += first
        m -= 1              # 반복문이 한 번씩 돌 때마다 1을 빼준다.
    if m == 0:
        break
    result += second
    m -= 1
'''

count = int(m/(k + 1)) * k + m % (k + 1)

result += count * first
result += (m - count) * second

print(result)