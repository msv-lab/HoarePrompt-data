maxn = 100005
mod = 1000000007
e = [[] for i in range(maxn)]
vis = [False for i in range(maxn)]

def func_1(u):
    sz = len(e[u])
    ok = True
    for i in range(sz):
        v = e[u][i][0]
        c = e[u][i][1]
        if vis[v] == False:
            if c == True:
                vis[v] = vis[u]
            else:
                vis[v] = -vis[u]
            ok = func_1(v)
        if c == 1 and vis[v] != vis[u]:
            return False
        if c == 0 and vis[v] != -vis[u]:
            return False
    return ok

def func_2():
    (n, m) = map(int, raw_input().split())
    for i in range(m):
        (u, v, c) = map(int, raw_input().split())
        u -= 1
        v -= 1
        e[u].append([v, c])
        e[v].append([u, c])
    cnt = 0
    for i in range(n):
        if vis[i] == False:
            vis[i] = True
            cnt += 1
            if func_1(i) == False:
                cnt = 0
                break
    ans = 1
    if cnt == 0:
        ans = 0
    for i in (1, cnt):
        ans *= 2
        ans %= mod
    print(ans)
func_2()