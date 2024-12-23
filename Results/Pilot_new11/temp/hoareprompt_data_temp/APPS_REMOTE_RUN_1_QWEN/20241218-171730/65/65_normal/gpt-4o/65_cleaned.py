(n, k) = map(int, input().split())
s = input()
color_count = {}
for color in s:
    if color in color_count:
        color_count[color] += 1
    else:
        color_count[color] = 1
can_distribute = True
for count in color_count.values():
    if count > k:
        can_distribute = False
        break
if can_distribute:
    print('YES')
else:
    print('NO')