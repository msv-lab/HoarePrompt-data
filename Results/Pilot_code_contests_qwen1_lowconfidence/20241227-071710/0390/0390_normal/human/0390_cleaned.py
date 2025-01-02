rints = lambda : [int(x) for x in stdin.readline().split()]
(n, m, d) = rints()
(c, ans) = (rints(), [0] * n)
(pos, su) = ([], 0)
for i in range(m - 1, -1, -1):
    pos.append(n + 1 - su - c[i])
    su += c[i]
pos.append(0)
pos.reverse()
for i in range(m):
    if pos[i + 1] - pos[i] <= d:
        for j in range(pos[i + 1], pos[i + 1] + c[i]):
            ans[j - 1] = i + 1
        continue
    pos[i + 1] = min(pos[i] + d, n)
    for j in range(pos[i + 1], pos[i + 1] + c[i]):
        ans[j - 1] = i + 1
    pos[i + 1] += c[i] - 1
if n + 1 - (pos[-1] + c[-1] - 1) > d:
    print('NO')
else:
    print('YES')
    print(' '.join(map(str, ans)))