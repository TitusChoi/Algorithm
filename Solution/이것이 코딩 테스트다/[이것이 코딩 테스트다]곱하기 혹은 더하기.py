# Title         : [이것이 코딩 테스트다]곱하기 혹은 더하기.py
# Description   : greedy

# 무조건 곱하기가 유리하다. 그러나 1과 0이 될 때는 무조건 더해야 한다.
n = input() # 데이터를 쪼개서 int 형태로 받는 것이 중요하다. 처음에는 string 형태, string은 하나의 리스트를 합산한 형태라고 생각하고 인덱스로 접근해야한다.

result = int(n[0])
string_len = len(n) # 시간복잡도 O(n)이므로 반복문에 넣지 않기 위해 정의

# 숫자가 하나 들어오는 경우
if string_len == 1:
    print(n)

# 숫자 스트링이 두 개 이상인 경우
for i in range(1, string_len):
    if i <= 1 or result <= 1: # 0, 1일 때는 무조건 더해야 함, 그러나 1행이 애초에 1이거나 0이어도 문제이므로 이때도 더해줘야 함
        result = result + int(n[i])
    else:
        result = result * int(n[i])

print(result)