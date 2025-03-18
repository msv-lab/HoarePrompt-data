for _ in range(int(input())):
    l1 = input().split()
    (n, k) = list(map(int, l1))
    if n == 1:
        print(k)
    else:
        arr = []
        k0 = k
        i = 0
        ans = []
        temp = 1
        while True:
            if temp * 2 < k:
                temp *= 2
                i += 1
            else:
                break
        ans.append((1 << i) - 1)
        ans.append(k - sum(ans))
        ans += [0] * (n - len(ans))
        print(*ans)