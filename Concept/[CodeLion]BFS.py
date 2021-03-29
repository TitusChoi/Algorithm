# Title         : [CodeLion]BFS.py
# Description   : BFS(Breadth-First-Search)

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft() # 바로 출력하기 위한 기법
        print(v, end = ' ') # pop된 자료 출력
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 리스트 자료형 표현
graph = [
    [], # 초기 index 0은 쓰지 않는다.
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 1부터 시작해보자
bfs(graph, 1, visited)