# Day 1

def average(list):
    if len(list) == 0:
        return 0
    return sum(list) / len(list)

def evenorodd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"