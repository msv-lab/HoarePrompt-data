def func_1(a, b, i, j):
    index = b[j:].find(a[i])
    if index != -1:
        return j + index
    else:
        return -1
t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    a = str(input())
    b = str(input())
    i = 0
    j = 0
    c = 0
    while j < m and i < n:
        new_j = func_1(a, b, i, j)
        if new_j != -1:
            j = new_j + 1
            i += 1
            c += 1
        else:
            break
    print(c)