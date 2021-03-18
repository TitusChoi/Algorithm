# Title         : [CodeLion_Day4]숫자 카드 게임.py
# Description   : greedy

# 쉬운 구현
n, m = map(int, input().split()) # m은 사용할 필요 없음!
result = 0

# # min, max로 바로 비교하는 기법

# for _ in range(n):
#     data = list(map(int, input().split()))
#     min_values = min(data)

#     result = max(result, min_values) # result와 min_values 값 자체를 비교

# 이중 반복문 활용 기법
# for _ in range(n):
#     data = list(map(int, input().split()))
#     min_values = min(data)

for _ in range(n):
    # 입력된 카드 행에서 최소 값 찾는 과정
    data = list(map(int, input().split())) # data.append(list(map(int, input().split())))
    min_value = 10001 # 조건보다 큰 값을 max로 설정
    for index in data:
        min_value = min(min_value, index)
    result = max(result, min_value)

print(result)

'''
input1
3 3
3 1 2
4 1 4
2 2 2

output1
2

input2
2 4
7 3 1 8
3 3 3 4

output2
3
'''