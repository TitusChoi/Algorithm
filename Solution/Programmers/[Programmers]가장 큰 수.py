# Title         : [Programmers]가장 큰 수.py
# Description   : sort
# Link          : https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer1 = list(map(str, numbers))
    answer2 = sorted(answer1, key=lambda x:x*3, reverse=True) # string 기준 sort를 활용할 수 있다.
    answer3 = str(int("".join(answer2))) # 0000과 같은 수 방지용으로 넣기
    return answer3

print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))
# print(solution([1000, 0, 5, 99, 100]))
# print(solution([0, 0, 0]))
# print(solution([0, 5, 10, 15, 20]))