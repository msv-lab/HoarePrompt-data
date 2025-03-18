from math import ceil

def func():
    t = int(input())
    for _ in range(t):
        (n, k) = map(int, input().split())
        if k % 2 == 0 and k // 2 % 2 == 1:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))

