# Title         : [Programmers]k번째수.py
# Description   : sort
# Link          : https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for index in commands:
        '''
        방법 1 : sorted
        temp = sorted(array[(index[0] - 1) : index[1]]) # sorted 함수 사용
        
        방법 2 : sort
        temp = array[(index[0] - 1) : index[1]]
        temp.sort() # sort 함수 사용
        '''

        temp = quick(array[(index[0] - 1) : index[1]])
        answer.append(temp[index[2] - 1]) # 정렬 사용해야 함

    return answer

def quick(array):
    n = len(array)

    if n <= 1:
        return array
    
    pivot = array[n // 2]

    greater, equal, less = [], [], []

    for i in array:
        if i > pivot:
            greater.append(i)
        elif i < pivot:
            less.append(i)
        else:
            equal.append(i)

    return quick(less) + equal + quick(greater) # 재귀 함수적 용법

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))