# Title         : [B1260]DFS와 BFS.py
# Description   : dfs/bfs

n, m, v=map(int,input().split()) # 첫 줄

# 이중 배열 느낌으로 미리 할당
matrix=[[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    x, y = map(int,input().split())
    matrix[x][y] = matrix[x][y] = 1

visit_list = [0]*(n + 1)

print(matrix)