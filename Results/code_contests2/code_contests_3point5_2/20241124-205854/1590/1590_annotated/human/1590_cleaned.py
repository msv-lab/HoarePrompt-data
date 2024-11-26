(n, s) = map(int, raw_input().split())
p = []
for i in range(n):
    (fi, ti) = map(int, raw_input().split())
    p.append((fi, ti))
p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
p.append((0, 0))
time_passed = 0
for i in range(n + 1):
    time_passed += s - p[i][0]
    s = p[i][0]
    if time_passed < p[i][1]:
        time_passed += p[i][1] - time_passed
print(time_passed)