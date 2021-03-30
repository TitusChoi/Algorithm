# Title         : [이것이 코딩 테스트다]시각.py
# Description   : implementation

'''
변형 문제 : 특정 숫자 n이 시간 안에 들어가 있는 경우 모두 세면 몇?
'''

n = int(input())
count = 0

# 모든 경우를 전부 다 세는 경우
for i in range(24):
    for j in range(60):
        for k in range(60):
            if str(n) in str(i) + str(j) + str(k):
                count += 1

print(count)