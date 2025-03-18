def func_1(n, k):
    k = k // 2
    l = list(range(1, n + 1))
    c = 0
    for i in range(n, -1, -2):
        c += 1
        if k == 0:
            return l
        if k < i - 1:
            return func_2(c, k, l)
        k = k - i + 1
        l = func_3(c, l)

def func_2(c, k, l):
    (x, y) = (l[-c], l[-c - k])
    (l[-c], l[-c - k]) = (y, x)
    return l

def func_3(c, l):
    (x, y) = (l[-c], l[c - 1])
    (l[c - 1], l[-c]) = (x, y)
    return l

def func_4():
    (n, k) = map(int, input().split())
    if k % 2:
        return (0, 0)
    if n % 2:
        max_k = (n ** 2 - 1) // 2
    else:
        max_k = n ** 2 // 2
    if max_k < k:
        return (0, 0)
    return (n, k)

def func_5(l):
    print('YES')
    for i in l:
        print(i, end=' ')
    print()
    return

def func_6():
    (n, k) = func_4()
    if n == 0:
        print('NO')
        return
    l = func_1(n, k)
    func_5(l)
    return
T = int(input())
for i in range(T):
    func_6()