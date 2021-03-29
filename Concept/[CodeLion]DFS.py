# Title         : [CodeLion]DFS.py
# Description   : DFS(Depth-First-Search)

'''
인접 행렬을 통해 그래프 구현하는 방법

INF = 99999999 # 무한 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [[0, 7, 5], [7, 0 , INF], [5, INF, 0]]

print(graph)
'''

'''
# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)] # [[], [], []]

# 노드 0에 연결된 노드 정보 저장, 7과 5가 간선(edge)이다.
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장
graph[2].append((0, 5))
'''

# DFS 메서드 정의
def dfs(graph, start, visited):
    
    # 현재 노드 방문 처리
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

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

# 방문 정보를 리스트 자료형으로 표현 : 배열
visited = [False] * 9

# 1부터 시작해보자
dfs(graph, 1, visited)