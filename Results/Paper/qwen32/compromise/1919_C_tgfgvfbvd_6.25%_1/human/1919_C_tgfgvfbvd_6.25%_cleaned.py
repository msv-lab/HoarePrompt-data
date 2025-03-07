for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    a = l[0]
    b = 0
    c = 0
    y = 0
    for y in range(1, n):
        if l[y] > l[y - 1]:
            b = l[y]
            break
    for x in range(y + 1, n):
        if l[x] > a and l[x] > b:
            if l[x] - a >= l[x] - b:
                a = l[x]
            else:
                b = l[x]
            c += 1
        elif l[x] < a and l[x] < b:
            if a - l[x] <= b - l[x]:
                a = l[x]
            else:
                b = l[x]
        elif a >= l[x]:
            a = l[x]
        else:
            b = l[x]
    print(c)