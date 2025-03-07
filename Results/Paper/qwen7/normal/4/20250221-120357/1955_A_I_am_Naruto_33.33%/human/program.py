for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if n > 1:
        ans1 = a * n
        ans2 = (b * n // 2) + (a * n % 2)
        print(min(ans1, ans2))
    else:
        print(a)