t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    while a and a[0] == 0:
        a.pop(0)
    while a and a[-1] == 0:
        a.pop()
    print(a)
    for i in range(len(a)):
        if a[i] == 0:
            res += 1
    print(res)