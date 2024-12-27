def appoint(x, l, h):
    if l <= x <= h:
        return 1
    else:
        return 0


N = int(input())
friends = [list(map(int, input().split())) for i in range(N)]
min_group = min(x[0] for x in friends)
max_group = max(x[0] for x in friends)

t = 0
ans = 1
for i in range(min_group, max_group):
    z = sum([appoint(i + 1, lo, hi) for lo, hi in friends])
    if i + 1 == z:
        ans = z
        t = 1
    if t == 1 and i + 1 != z:
        break

print(ans - 1)