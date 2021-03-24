# Title         : [CodeLion]Recursive.py
# Description   : recursive

# def recursive_function(n):
#     if n == 100:
#         return
#     print(n, "번째 재귀 함수에서", n + 1, "번째 재귀 함수를 호출합니다.")
#     recursive_function(n + 1)
#     print(n, "번째 재귀 함수를 종료합니다.") # stack 자료구조와 유사하다. LIFO 형태를 띄고 있다.

# recursive_function(1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print("iterative factorial :", factorial_iterative(5))
print("recursive factorial :", factorial_recursive(5))