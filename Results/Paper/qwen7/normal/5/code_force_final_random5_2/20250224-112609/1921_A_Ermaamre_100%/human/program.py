t = int(input())
for _ in range(t):
    a = [[int(x) for x in input().split()] for i in range(4)]
    x = [p[0] for p in a]
    dx = max(x) - min(x)
    print(dx * dx)