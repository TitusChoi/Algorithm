# Title         : [CodeLion]DP.py
# Description   : Dynamic Programming

# 1. 메모제이션 하향식

# 메모할 메모리 할당, 캐싱(caching), 탑다운 방식
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    # 아직 계산하지 않은 문제라면 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print((fibo(99)))

# 보텀업 방식
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])