t = int(input())
for tc in range(t):
    (n, m) = map(int, input().split())
    gr = []
    for i in range(n):
        gr.append(input())
    ans = 'YES'
    if gr[0][0] != gr[n - 1][m - 1]:
        impossible = True
        for j in range(m - 1):
            if gr[0][j] != gr[0][j + 1] or gr[n - 1][j] != gr[n - 1][j + 1]:
                impossible = False
        if impossible:
            ans = 'NO'
        impossible = True
        for i in range(n - 1):
            if gr[i][0] != gr[i + 1][0] or gr[i][m - 1] != gr[i + 1][m - 1]:
                impossible = False
        if impossible:
            ans = 'NO'
    print(ans)