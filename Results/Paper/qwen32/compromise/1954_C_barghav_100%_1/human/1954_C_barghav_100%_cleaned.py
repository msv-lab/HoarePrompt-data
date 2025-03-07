def func_1():
    a = list(input())
    b = list(input())
    f = 0
    for i in range(len(a)):
        if f == 0:
            if a[i] < b[i]:
                (a[i], b[i]) = (b[i], a[i])
                f = 1
            elif a[i] > b[i]:
                f = 1
        elif a[i] > b[i]:
            (a[i], b[i]) = (b[i], a[i])
    for i in range(len(a)):
        print(a[i], end='')
    print()
    for i in range(len(b)):
        print(b[i], end='')
    print()
t = int(input())
for _ in range(t):
    func_1()