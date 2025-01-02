from sys import stdin, stdout
from collections import defaultdict
from itertools import repeat
def solve():
    n = int(stdin.readline())
    a = [map(int, stdin.readline().split()) for _ in xrange(n - 2)]
    s = defaultdict(set)
    for i, t in enumerate(a):
        x, y, z = t
        if x < y:
            s[x,y].add(i)
        else:
            s[y,x].add(i)
        if y < z:
            s[y,z].add(i)
        else:
            s[z,y].add(i)
        if x < z:
            s[x,z].add(i)
        else:
            s[z,x].add(i)
    con = [[] for _ in xrange(n + 1)]
    c = [3] * (n - 2)
    st = []
    po = st.pop
    pu = st.append
    for k, v in s.viewitems():
        if len(v) == 1:
            i = v.pop()
            c[i] -= 1
            if c[i] == 1:
                pu(i)
            x, y = k
            con[y].append(x)
            con[x].append(y)
    q = []
    while st:
        i = po()
        if c[i] == 1:
            x, y, z = a[i]
            if x < y and i in s[x,y]:
                k = x, y
                q.append(z)
            elif x > y and i in s[y,x]:
                k = y, x
                q.append(z)
            elif y < z and i in s[y,z]:
                k = y, z
                q.append(x)
            elif y > z and i in s[z,y]:
                k = z, y
                q.append(x)
            elif x < z and i in s[x,z]:
                k = x, z
                q.append(y)
            else:
                k = z, x
                q.append(y)
            c[i] -= 1
            s[k].remove(i)
            j = s[k].pop()
            c[j] -= 1
            if c[j] == 1:
                pu(j)
        else:
            x, y, z = a[i]
            if x not in q:
                q.append(x)
            elif y not in q:
                q.append(y)
            else:
                q.append(z)
    p = []
    x = 1
    d = [0] * (n + 1)
    for i in xrange(n):
        d[x] = 1
        p.append(x)
        for y in con[x]:
            if not d[y]:
                x = y
                break
    stdout.write(' '.join(map(str, p)))
    stdout.write('\n')
    stdout.write(' '.join(map(str, q)))
    stdout.write('\n')

T = int(stdin.readline())
for _ in xrange(T):
    solve()
