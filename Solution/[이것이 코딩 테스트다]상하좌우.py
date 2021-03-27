# Title         : [이것이 코딩 테스트다]상하좌우.py
# Description   : implementation

n = int(input())
x, y = 1, 1

plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)): # L, R, U, D와 dx, dy를 매칭
        if plan == move_types[i]:
            nx = x + dx[i] # 매칭된 움직임
            ny = y + dy[i] # 매칭된 움직임
    
    if nx < 1 or ny < 1 or nx > n or ny > n: # 벗어날 경우 별도의 모션을 취하지 않는다.
        continue
    x, y = nx, ny

print(x, y)

'''
5
R R R U D D
'''