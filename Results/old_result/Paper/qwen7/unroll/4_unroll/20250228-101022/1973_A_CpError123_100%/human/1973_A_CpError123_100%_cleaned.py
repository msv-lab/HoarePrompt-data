t = int(input())
for _ in range(t):
    (a, b, c) = map(int, input().split())
    if (a + b + c) % 2 != 0:
        print(-1)
        continue
    x = (a + b + c) // 2
    y = a + b
    print(min(x, y))