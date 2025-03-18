for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    (a, b) = (float('inf'), float('inf'))
    c = 0
    for x in range(n):
        if a > b:
            (a, b) = (b, a)
        if l[x] <= a:
            a = l[x]
        elif l[x] <= b:
            b = l[x]
        else:
            a = l[x]
            c += 1
    print(c)