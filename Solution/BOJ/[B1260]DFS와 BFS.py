# Title         : [B1260]DFS와 BFS.py
# Description   : dfs/bfs

from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    line = list(map(int, stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

def dfs(start, visited):
    matrix_length = len(matrix[start]) # 시간복잡도 줄이기
    visited += [start] # stack 형태로 구현
    print(start, end = ' ') # pop된 자료 그 자리에서 바로 출력
    for k in range(matrix_length):
        if matrix[start][k] == 1 and k not in visited:
            dfs(k, visited) # 재귀함수 꼴로 구현
    return visited


def bfs(start):
    matrix_length = len(matrix[start]) # 시간복잡도 줄이기
    visited = [start]
    queue = deque([start])
    while queue: # queue가 존재할 때 동작시키기
        n = queue.popleft() # 자료 계속 빼주기
        print(n, end = ' ') # 빼준 값 출력
        for k in range(matrix_length):
            if matrix[n][k] == 1 and k not in visited:
                visited.append(k)
                queue.append(k)
    return visited

dfs(v,[]) # 시작, []는 굳이 정의 안해도 괜찮음
print()
bfs(v)

'''
input 1
4 5 1
1 2
1 3
1 4
2 4
3 4

output 1
1 2 4 3
1 2 3 4
'''

'''
input 2
5 5 3
5 4
5 2
1 2
3 4
3 1

output 2
3 1 2 5 4
3 1 4 2 5
'''