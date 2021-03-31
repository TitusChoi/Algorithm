# Title         : [Programmers]타겟 넘버.py
# Description   : dfs/bfs
# Link          : https://programmers.co.kr/learn/courses/30/lessons/43165

# bfs 풀이
from collections import deque

def solution_bfs(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # sum, level
    while queue:
        s, l = queue.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))

    return answer

'''
# dfs 풀이
def solution_dfs(numbers, target):
    answer = 0
    stack = [] # sum, level
    dfs = ()

    return answer
'''

print(solution_bfs([1, 1, 1, 1, 1], 3))
# print(solution_dfs([1, 1, 1, 1, 1], 3))