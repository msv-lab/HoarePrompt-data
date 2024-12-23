(n, k) = map(int, input().split())
s = input()
color_count = {}
for c in s:
    if c in color_count:
        color_count[c] += 1
    else:
        color_count[c] = 1
max_color_count = max(color_count.values())
if max_color_count <= k:
    print('YES')
else:
    print('NO')