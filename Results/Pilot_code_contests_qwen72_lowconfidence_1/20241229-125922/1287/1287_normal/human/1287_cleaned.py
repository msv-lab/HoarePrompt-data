rints = lambda : [int(x) for x in stdin.readline().split()]
(n, m, q) = rints()
(a, b, ans) = (rints(), Counter(rints()), [])
all = len(b)
for i in range(q):
    (dis, mem) = (set(), Counter())
    if int(ceil((n - i) / q)) < m:
        break
    for j in range(i, i + (m - 1) * q, q):
        mem[a[j]] += 1
    for (k, j) in mem.items():
        if j == b[k]:
            dis.add(k)
    be = i
    for j in range(i + (m - 1) * q, n, q):
        mem[a[j]] += 1
        if mem[a[j]] == b[a[j]]:
            dis.add(a[j])
        else:
            dis.discard(a[j])
        if len(dis) == all:
            ans.append(be + 1)
        mem[a[be]] -= 1
        if b[a[be]] and mem[a[be]] == b[a[be]]:
            dis.add(a[be])
        else:
            dis.discard(a[be])
        be += q
print('%d\n%s' % (len(ans), ' '.join(map(str, sorted(ans)))))