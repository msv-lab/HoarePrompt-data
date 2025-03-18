def func_1():
    a = list(input())
    b = list(input())
    for i in range(len(a)):
        if i <= len(a) // 2 - 1:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = m
            b[i] = n
        else:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = n
            b[i] = m
    for i in range(len(a)):
        print(a[i], end='')
    print()
    for i in range(len(b)):
        print(b[i], end='')
    print()
t = int(input())
for _ in range(t):
    func_1()