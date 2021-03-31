# Title         : [Concept]Search.py
# Description   : search

example = [116, 573, 223, 34, 61, 14, 111, 222, 33, 16, 17, 12, 617, 231, 55, 23, 62, 316]

def sequential_search(array, target):
    n = len(array)
    for i in range(n):
        if array[i] == target:
            return i + 1

def binary_search(array, target, start, end): # start = start index, end = end index 숫자가 아님!
    if start > end:
        return None

    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
        

print(sequential_search(example, 61))
example.sort()
print(example)
print(binary_search(example, 61, 0, len(example) - 1) - 1)