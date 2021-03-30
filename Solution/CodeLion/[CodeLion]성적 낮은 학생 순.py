# Title         : [CodeLion]성적 낮은 학생 순.py
# Description   : sorting

n = int(input()) # 학생수
scores = []

for _ in range(n):
    scores.append(input().split()) # map 쓸 수 없음
    scores[_][1] = int(scores[_][1]) # 비교를 위한 정수화

# key method 활용
scores.sort(key=lambda x:x[1]) # 두번째 람다를 기준으로 sorting, 핵심 알고리즘

# 특정 index만 출력
for _ in range(n):
    print(scores[_][0], end=' ')

'''
2
홍길동 95
이순신 77
'''