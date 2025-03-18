for i in range(int(input())):
    (n, m) = map(int, input().split())
    k = abs(n - m)
    if k & k - 1 == 0:
        print(k)
    elif k % 2 != 0:
        print(1)
    else:
        l = bin(k).replace('0b', '')
        p = len(l)
        q = 2 ** (p - 1)
        f = k - q
        while f & f - 1 != 0:
            l = bin(f).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            f = f - q
        print(f)