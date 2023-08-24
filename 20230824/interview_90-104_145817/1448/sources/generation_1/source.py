n, d = map(int, input().split())
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    if (0 <= x <= n) and (d <= y <= n-d+x) and (y >= -x+d):
        print("YES")
    else:
        print("NO")
    