def func():
    t = int(input())
    for _ in range(t):
        (n, k) = map(int, input().split())
        n_back = n
        s = (n + 1) // 2
        n = (n + 1) // 2
        m = 1
        while s < k:
            if n == 0:
                s = n_back
                n = 1
                break
            m *= 2
            n //= 2
            s += n
        print((2 * (k - (s - n)) - 1) * m)

