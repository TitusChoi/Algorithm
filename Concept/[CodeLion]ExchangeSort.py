# Title         : [CodeLion]InsertionSort.py
# Description   : sorting

def exchange_sort(array):
    n = len(array) # 크기 정의, 불필요한 반복문 제거
    for i in range(n - 1): # 최대 크기보다 하나 적은 영역까지 비교
        for j in range(i + 1,n): # 역순으로 비교해가면서 sort
            if(array[i] > array[j]): # 크면 교환
                array[i], array[j] = array[j], array[i] # 실제 swap
    return array

print(exchange_sort([-1, 10, 7, 11, 5]))