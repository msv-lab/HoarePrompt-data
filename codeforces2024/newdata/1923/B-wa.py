for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = sorted(map(lambda x: abs(int(x)), input().split()))

    last_pos = 0
    bullets = 0
    for i in range(n):
        bullets += k * (x[i] - last_pos)
        last_pos = x[i]
        bullets -= a[i]
        if bullets < 0:
            print('NO')
            break
    else:
        print('YES')
