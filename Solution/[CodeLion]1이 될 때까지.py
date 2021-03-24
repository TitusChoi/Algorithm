# Title         : [CodeLion]1이 될 때까지.py
# Description   : greedy

n, k = map(int, input().split())
result = 0

while n != 1: # n은 1이 될 때까지
    if n % k == 0: # 나누어 떨어지는 경우
        n = n // k
        result += 1
    else: # 나누어 떨어지지 않는 경우
        n -= 1
        result += 1

print(result)