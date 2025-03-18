for _ in range(int(input())):
    (n, k) = map(int, input().split())
    print(n if n - k > 1 else 1)