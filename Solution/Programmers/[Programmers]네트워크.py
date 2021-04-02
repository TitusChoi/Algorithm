# Title         : [Programmers]네트워크.py
# Description   : dfs/bfs
# Link          : https://programmers.co.kr/learn/courses/30/lessons/43162

def dfs(n, computers, start, visited):
    visited[start] = True # 왔다 표시해주기
    for other in range(n):
        if other != start and computers[start][other] == 1 and visited[other] == False: # 연결된 컴퓨터가 존재안하고, 아직 True라고 반환안한 곳
            dfs(n, computers, other, visited)


def solution(n, computers):
    answer = 0
    # 방문한 판단 노드를 따로 만들어준다. n만큼 false를 할당
    visited = [False for _ in range(n)]
    for start in range(n):
        if visited[start] == False:
            dfs(n, computers, start, visited) # 돌아가면
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))