(l, r, a) = map(int, input().split())
if l < r:
    l += min(a, r - l)
    a -= min(a, r - l)
elif r < l:
    r += min(a, l - r)
    a -= min(a, l - r)
max_team_size = l + r + a // 2 * 2
if max_team_size % 2 != 0:
    max_team_size -= 1
print(max_team_size)