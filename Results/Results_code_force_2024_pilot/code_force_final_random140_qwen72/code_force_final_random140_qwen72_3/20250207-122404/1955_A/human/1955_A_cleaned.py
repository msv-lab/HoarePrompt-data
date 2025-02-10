for _ in range(int(input())):
    (n, a, b) = map(int, input().split())
    s1 = n * a
    s2 = b * (n // 2) + n % 2 * a
    print(min(s1, s2))