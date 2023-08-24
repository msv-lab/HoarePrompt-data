n, d = map(int, input().split())
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    if (d <= x <= n-d) and (0 <= y <= n-d+x) and (y >= -x+d if x < n-d else y >= -x+n):
        print("YES")
    else:
        print("NO")