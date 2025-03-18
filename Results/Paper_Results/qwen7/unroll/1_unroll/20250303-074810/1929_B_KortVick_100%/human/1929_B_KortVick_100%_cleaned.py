t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    if 4 * n - 2 == k:
        print(k // 2 + 1)
    else:
        print(ceil(k / 2))