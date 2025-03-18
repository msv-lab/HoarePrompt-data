def func():
    for line in [*open(0)][1:]:
        (p, q, r) = map(int, line.split())
        q += r
        print((p - q // 3, -1)[r < q % 3])

