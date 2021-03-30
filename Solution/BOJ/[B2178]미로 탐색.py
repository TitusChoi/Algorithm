# Title         : [B2178]미로 탐색.py
# Description   : dfs/bfs

n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input()))) # 한 칸씩 띄어서 받는 기법

# 이 문제는 bfs로 접근해야 최소개수로 찾을 수 있다.

from collections import deque

# 4 방향 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # start 지점

    # queue 존재할 때
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 4방향 정의해서 움직이기
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1: # 길 찾은 경우
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n-1][m-1] # 최종 출력은 index를 하나씩 줄여야 도착지점을 찾는 것이다.

print(bfs(0, 0)) # maze를 보면 즉, 지난 길을 모두 더했음을 알 수 있다. 원래 maze는 훼손!

'''
4 6
101111
101010
101011
111011

4 6
110110
110110
111111
111101

2 25
1011101110111011101110111
1110111011101110111011101

7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
'''