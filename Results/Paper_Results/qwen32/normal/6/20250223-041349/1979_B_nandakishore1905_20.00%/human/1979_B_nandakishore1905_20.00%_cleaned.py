for i in range(int(input())):
    (n, m) = map(int, input().split())
    k = abs(n - m)
    if k & k - 1 == 0:
        print(k)
    elif n == 0 and m % 2 != 0:
        print(1)
    elif n == 0 and m % 2 == 0:
        print(2)
    else:
        l = bin(k).replace('0b', '')
        p = len(l)
        q = 2 ** (p - 1)
        print(k - q)