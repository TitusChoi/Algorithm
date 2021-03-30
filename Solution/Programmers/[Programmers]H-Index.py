# Title         : [Programmers]H-Index.py
# Description   : sort
# Link          : https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    n = len(citations) # 발표논문수, 제한조건
    citation = sorted(citations, reverse = True)
    # 6 5 3 1 0 
    
    h = 0 # H-index 지표
    for numbers in citation:
        if numbers > h: # h
            h += 1
    return h

print(solution([3, 0, 6, 1, 5]))