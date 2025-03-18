t = int(input())
for itest in range(0, t, 1):
    (n, m, k) = map(int, input().split())
    if n <= k or n - math.ceil(n / m) <= k:
        print('NO')
    else:
        print('Yes')