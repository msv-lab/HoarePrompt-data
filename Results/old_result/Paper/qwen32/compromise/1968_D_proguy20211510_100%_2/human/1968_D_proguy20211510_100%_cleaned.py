(YES, NO) = ('YES', 'NO')
MOD = 10 ** 9 + 7
alpha = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(int(input())):
    (n, k, pb, ps) = input().split()
    (n, k, pb, ps) = (int(n), int(k), int(pb), int(ps))
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    (pathb, paths) = ([], [])
    vis = [0] * n
    vis[pb - 1] = 1
    while True:
        pathb.append(a[pb - 1])
        pb = p[pb - 1]
        if vis[pb - 1] == 1:
            break
    vis = [0] * n
    vis[ps - 1] = 1
    while True:
        paths.append(a[ps - 1])
        ps = p[ps - 1]
        if vis[ps - 1] == 1:
            break
    (resb, ress) = (0, 0)
    (preb, pres) = (0, 0)
    for i in range(len(pathb)):
        if k < i + 1:
            break
        curr = preb + pathb[i] * (k - i)
        preb += pathb[i]
        resb = max(resb, curr)
    for i in range(len(paths)):
        if k < i + 1:
            break
        curr = pres + paths[i] * (k - i)
        pres += paths[i]
        ress = max(ress, curr)
    if resb > ress:
        print('Bodya')
    elif ress > resb:
        print('Sasha')
    else:
        print('Draw')