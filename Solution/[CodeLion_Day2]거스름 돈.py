# Title         : [CodeLion_Day2]거스름 돈.py
# Description   : greedy

N = 1260 # 임의의 돈

def greedy(n):
    count = 0
    coin_types = [500, 100, 50, 10]

    # 반복문과 나머지, 몫
    for coin in coin_types:
        count += n // coin # 0->2->2->1->1
        n %= coin # 260->60->10->0

    return count

print(greedy(N))