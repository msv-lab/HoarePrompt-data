for s in [*open(0)][1:]:
    (n, k) = map(int, s.split())
    if k <= 4 * n - 4:
        print(math.ceil(k / 2))
    elif k == 4 * n - 3:
        print(2 * n - 1)
    elif k == 4 * n - 2:
        print(2 * n)