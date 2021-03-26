# Title         : [Programmers]더 맵게.py
# Description   : heap
# Link          : https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    heapq.heapify(scoville) # 최소 힙
    
    count = 0
        
    while(scoville[0] < K):
        temp_scoville1 = heapq.heappop(scoville)
        temp_scoville2 = temp_scoville1 + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, temp_scoville2)
        count += 1
        
        if len(scoville) == 1 and scoville[0] < K: # 예외 처리
            return -1
    
    return count

print(solution([1, 2, 3, 9, 10, 12], 7))