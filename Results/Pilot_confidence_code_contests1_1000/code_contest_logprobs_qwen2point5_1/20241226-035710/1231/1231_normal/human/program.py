from collections import deque

ispow2 = lambda x: x and (not (x & (x - 1)))
n, cur, ans = int(input()), 0, []

for i in range(n):
    tem = deque(range(cur, cur + n))
    while i and not ispow2(tem[0] - ans[-1][0]):
        tem.rotate(-1)
    ans.append(tem)
    cur += n

print('\n'.join([' '.join(map(str, x)) for x in ans]))
