# Title         : [CodeLion_Day5]팝퀴즈.py
# Description   : 16번, 17번 문제

# Q1 : 친구 키 비교 문제

def pop_quick(array):
    n = len(array)
    if n <= 1: # 항상 무조건 넣어줘야 error 안난다!!!!! 분할 합병이므로 무조건 영향미침
        return array
    pivot = array[n // 2]
    less, equal, greater = [], [], []
    for i in array:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)
    return pop_quick(less) + equal + pop_quick(greater)    

# def pop_insertion(array):
#     n = len(array) # len 함수도 for문이므로 시간복잡도 해결을 위해 제거
    
#     if n <= 1:
#         return array
#     for i in range(1, n):
#         j = i - 1
#         key = array[i]
#         while j >= 0 and array[j] > key: # key랑 같아질 경우 끝냄!
#             array[j + 1] = array[j] # 오른쪽으로 한 칸 밀기
#             j -= 1
#         array[j + 1] = key # 비어있는 왼쪽 칸에 key 값 넣기 빼줘서 그렇지 array[j]랑 같음
#     return array

friends = list(map(int, input().split())) # 160 175 171 170 입력 예시
print(pop_quick(friends))

# # Q2 : 입력된 값 합 구하기 문제
# n = map(int, input().split())
# result = 0
# for i in n:
#     result += i
# print(result)