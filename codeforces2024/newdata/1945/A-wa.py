from math import ceil
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    extra = b%3
    if extra and 3 - extra > c:
        print(-1)
    else:
        if 3 - extra <= c:
            c -= 3 - extra
        print(a + ceil(b/3) + ceil(c/3))
