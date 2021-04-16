array = list(input()) # 리스트 형태로 입력 받기
n = len(array)
sum = 0
for i in array:
	sum += int(i)
print(sum)
