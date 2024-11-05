n, t = map(int, input().split())
buses = []
for _ in range(n):
    s, d = map(int, input().split())
    buses.append((s, d))

min_time = float('inf')
ans = -1
for i, (s, d) in enumerate(buses):
    time = (t - s) % d
    if time < min_time:
        min_time = time
        ans = i + 1
print(ans)
