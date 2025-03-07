t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    # mas = []
    # while n:
    #     mas.append((n + 1) // 2)
    #     n //= 2
    # print(mas)
    # continue
    s = 0
    m = 1
    while n:
        x = ((n + 1) // 2)
        n //= 2
        if (s < k) and (k <= s + x):
            break
        s += x
        m *= 2
    print((2 * (k - s) - 1) * m)
 
    # n_back = n
    # s = (n + 1) // 2
    # n = (n + 1) // 2
    # m = 1
    # while s < k:
    #     if n == 0:
    #         s = n_back
    #         n = 1
    #         break
    #     m *= 2
    #     n //= 2
    #     s += n
    # # print(n, s, k, m, (k - (s - n)))
    # print((2 * (k - (s - n)) - 1) * m)