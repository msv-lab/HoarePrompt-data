for _ in range(int(input())):
    (n, a, b) = map(int, input().split())
    if n % 2:
        if 2 * a < b:
            print(a * n)
        else:
            print(n // 2 * b + a)
    elif 2 * a < b:
        print(a * n)
    else:
        print(n // 2 * b)