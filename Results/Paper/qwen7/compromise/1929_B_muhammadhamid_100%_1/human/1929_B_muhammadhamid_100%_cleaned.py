for _ in range(int(input())):
    (n, k) = map(int, input().split())
    if k == 1:
        print(1)
        continue
    if k <= 2 * (n + (n - 2)):
        print(math.ceil(k / 2))
    else:
        print(k // 2 + 1)