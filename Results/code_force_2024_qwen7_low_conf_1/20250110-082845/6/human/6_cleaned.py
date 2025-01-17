for t in range(int(input())):
    (n, k) = map(int, input().split())
    r = n
    if k >= n - 1:
        r = 1
    print(r)