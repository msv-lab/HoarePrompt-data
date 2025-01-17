t = int(input())

for i in range(t):
    n = int(input())
    a = list(input())
    b = list(input())
    c = list(input())
    for k in range(n):
        if a[k] == b[k] and a[k] == c[k] and b[k] == c[k]:
            continue
        if a[k] == c[k] or b[k] == c[k]:
            print('NO')
            break
        if k == len(a) - 1 and a[k] != c[k] and b[k] != c[k]:
            print('YES')
            break