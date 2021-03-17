# Day 1

def average(array):
    if len(array) == 0:
        return 0
    return sum(array) / len(array)

def evenorodd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"