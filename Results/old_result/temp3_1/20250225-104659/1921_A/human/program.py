import math

def func():
    t = int(input())
    for steps in range(t):
        (a, b) = map(int, input().split())
        (c, d) = map(int, input().split())
        (e, f) = map(int, input().split())
        (g, h) = map(int, input().split())
        n = (a - c) * (a - c) + (b - d) * (b - d)
        x = (a - e) * (a - e) + (b - f) * (b - f)
        if x > n:
            print(n)
        else:
            print(x)

