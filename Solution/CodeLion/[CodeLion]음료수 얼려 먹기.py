# Title         : [CodeLion]음료수 얼려 먹기.py
# Description   : dfs

n, m = map(int, input().split()) # 행과 열 입력
graph = []

for _ in range(n):
    graph.append(list(map(int, input()))) # 붙여서 쓸 경우에 append 활용

def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    
    if graph[x][y] == 0: # 얼음 발견
        graph[x][y] = 1  # 발견한 얼음은 사용한다.
        
        # 상하좌우 재귀적 용법
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)