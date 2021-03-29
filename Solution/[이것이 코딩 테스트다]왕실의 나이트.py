# Title         : [이것이 코딩 테스트다]왕실의 나이트.py
# Description   : implementation

position = input()
position_letter = ord(position[0]) - ord('a') + 1 # 아스키코드를 int형태로 변경해서 활용
position_number = int(position[1])

# 나이트 이동방향 정의
steps = [(2, 1), (1, 2), (-2, -1), (-1, -2), (-2, 1), (2, -1), (-1, 2), (1, -2)]

move = 0
for step in steps:
    next_position_letter = position_letter + step[0]
    next_position_number = position_number + step[1]
    if next_position_number >= 1 and next_position_number <= 8 and next_position_letter >= 1 and next_position_letter <= 8:
        move += 1

print(move)