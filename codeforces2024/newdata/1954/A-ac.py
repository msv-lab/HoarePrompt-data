t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    max_color = (n + m - 1) / m
    if max_color + k >= n:
        print('NO')
    else:
        print('YES')
    