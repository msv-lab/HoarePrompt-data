def getpd(x):
    # Find the parent of x with path compression and calculate the distance parity
    if P[x] == x:
        return x, 0
    p, d = getpd(P[x])
    dd = D[x] + d
    P[x] = p
    D[x] = dd
    return p, dd

# Read input dimensions and number of queries
n, m, q = map(int, input().split())
# Read the grid
a = [list(input()) for _ in range(n)]
# Initialize distance array and BFS queue
v = [[-1] * m for _ in range(n)]
queue = []
rx, ry = None, None

# Initialize BFS queue with volcano positions and find an island cell
for x in range(n):
    for y in range(m):
        if a[x][y] == 'v':
            queue.append((x, y))
            v[x][y] = 0
        elif a[x][y] == '#':
            rx, ry = x, y

# Perform BFS to calculate minimum distances to volcanoes
i = 0
while i < len(queue):
    x, y = queue[i]
    i += 1
    for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= xx < n and 0 <= yy < m and v[xx][yy] < 0:
            v[xx][yy] = v[x][y] + 1
            queue.append((xx, yy))

# Initialize union-find structures
P = list(range(n * m))
D = [0] * (n * m)
S = [1] * (n * m)
ans = [None] * (n * m)
C = [[i] for i in range(n * m)]
reach = [[False] * m for _ in range(n)]

# Process cells in reverse order of BFS
for i in range(len(queue) - 1, -1, -1):
    x, y = queue[i]
    if a[x][y] == '#':
        continue
    reach[x][y] = True
    for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= xx < n and 0 <= yy < m and reach[xx][yy]:
            ap, ad = getpd(x * m + y)
            bp, bd = getpd(xx * m + yy)
            asz = S[ap]
            bsz = S[bp]
            delta = y > ry and (x == rx and xx == rx - 1 or x == rx - 1 and xx == rx)
            cl = None

            if ap != bp:  # join
                if asz > bsz:
                    D[bp] = (delta + bd + ad) % 2
                    P[bp] = ap
                    S[ap] = asz + bsz
                    if not C[ap] or not C[bp]:
                        cl = ap
                    C[ap] = [C[ap], C[bp]]
                else:
                    D[ap] = (delta + bd + ad) % 2
                    P[ap] = bp
                    S[bp] = asz + bsz
                    if not C[ap] or not C[bp]:
                        cl = bp
                    C[bp] = [C[bp], C[ap]]
            else:  # cycle
                if (ad + bd + delta) % 2 == 1:
                    cl = ap
            if cl is not None:
                vv = v[x][y]
                st = C[cl]
                while st:
                    u = st.pop()
                    if isinstance(u, list):
                        for uu in u:
                            st.append(uu)
                    else:
                        ans[u] = vv

# Answer each query
res = []
for _ in range(q):
    x, y = map(int, input().split())
    res.append(str(ans[(x - 1) * m + (y - 1)]))
print('\n'.join(res))