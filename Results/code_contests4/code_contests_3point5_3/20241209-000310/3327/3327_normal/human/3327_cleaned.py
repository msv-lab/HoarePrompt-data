pr = stdout.write
raw_input = stdin.readline

def func_1():
    return int(raw_input())

def func_2():
    return list(map(int, raw_input().split()))

def func_3(n):
    stdout.write(str(n) + '\n')

def func_4(arr):
    pr(' '.join(map(str, arr)) + '\n')

def func_5():
    return map(int, stdin.read().split())
range = xrange
(n, m) = func_2()
d = [[] for i in range(n + 1)]
for i in range(m):
    (u, v) = func_2()
    d[u].append(v)
    d[v].append(u)
arr = []
vis = [0] * (n + 1)
for i in range(1, n + 1):
    if not vis[i]:
        vis[i] = 1
        q = [i]
        mn = i
        mx = i
        while q:
            x = q.pop()
            mn = min(mn, x)
            mx = max(mx, x)
            for j in d[x]:
                if not vis[j]:
                    vis[j] = 1
                    q.append(j)
        arr.append((mn, mx))
ans = 0
(px, py) = arr[0]
n1 = len(arr)
for i in range(1, n1):
    (x, y) = arr[i]
    if x <= py:
        ans += 1
    px = min(x, px)
    py = max(y, py)
func_3(ans)