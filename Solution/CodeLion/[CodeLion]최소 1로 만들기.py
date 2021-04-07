# Title         : [CodeLion]최소 1로 만들기.py
# Description   : Dynamic Programming

x = int(input()) # 특정 x값 찾기

# 앞서 계산된 결과를 저장하기 위한 테이블 만들기
d = [0] * 30001

# 다이나믹 프로그래밍 (Dynamic Programming), 나누는 수는 소수로 주어질 수 밖에 없다라는 점을 활용
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우의 값을 현재 위치에 저장
    d[i] = d[i - 1] + 1

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
    