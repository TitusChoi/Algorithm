# Title         : [CodeLion]미로 탈출.py
# Description   : bfs

from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간 벗어난 경우 & 벽인 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 0:
                continue

            # 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1: # 처음 방문하는 경우
                graph[nx][ny] = graph[x][y] + 1 # 처음 방문하는 경우, 전에 있었던 위치에 1씩 더함
                # 최종 위치에 도달하게 되면 더할게 없어서 반복문 탈출
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0)) # 초기 시작위치 바꿀 수 있음
'''
input 1
4 6
101111
101010
101011
111011

output 1
15

input 2
4 6
110110
110110
111111
111101

output 2
9
'''