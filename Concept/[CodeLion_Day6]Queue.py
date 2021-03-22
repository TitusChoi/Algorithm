# Title         : [CodeLion_Day6]Queue.py
# Description   : Queue

from collections import deque

queue = deque()
queue.append(5)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.popleft() # 왼쪽으로 밀기
print(queue)
queue.append(7)
print(queue)
queue.append(1)
print(queue)
queue.append(4)
print(queue)
queue.popleft() # 왼쪽으로 밀기
print(queue)