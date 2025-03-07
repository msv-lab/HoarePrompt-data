def main():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
 
    tot = 0
    bipartite = True
 
    def dfs(i):
        nonlocal tot, bipartite
        if not visited[i]:
            visited[i] = True
            tot += coef[i]
            for j in range(n):
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                if (r[i] + r[j]) ** 2 == dx ** 2 + dy ** 2:
                    if not visited[j]:
                        coef[j] = -coef[i]
                        dfs(j)
                    else:
                        bipartite = bipartite and coef[j] == -coef[i]
 
    ok = False
    for i in range(n):
        if not visited[i]:
            coef[i] = 1
            tot = 0
            bipartite = True
            dfs(i)
            ok = ok or (bipartite and tot != 0)
    if ok:
        print("YES")
    else:
        print("NO")
 
main()