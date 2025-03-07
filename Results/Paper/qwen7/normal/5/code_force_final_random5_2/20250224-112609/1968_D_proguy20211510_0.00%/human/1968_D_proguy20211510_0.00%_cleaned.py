(YES, NO) = ('YES', 'NO')
MOD = 10 ** 9 + 7
alpha = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(int(input())):
    (n, k, pb, ps) = input().split()
    (n, k, pb, ps) = (int(n), int(k), int(pb), int(ps))
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    maxa = max(a)
    if a[pb - 1] == a[ps - 1] == maxa:
        print('Draw')
        continue
    elif a[pb - 1] == maxa:
        print('Bodya')
        continue
    elif a[ps - 1] == maxa:
        print('Sasha')
        continue
    (b, s) = ([], [])
    (founds, foundb) = (False, False)
    for i in range(k):
        if foundb and founds:
            b.append((k - (i + 1)) * maxa)
            s.append((k - (i + 1)) * maxa)
            break
        if foundb:
            b.append(maxa)
        elif a[pb - 1] == maxa:
            foundb = True
            b.append(a[pb - 1])
        else:
            b.append(a[pb - 1])
            pb = p[pb - 1]
        if founds:
            s.append(maxa)
        elif a[ps - 1] == maxa:
            founds = True
            s.append(a[ps - 1])
        else:
            s.append(a[ps - 1])
            ps = p[ps - 1]
    (preb, pres) = ([], [])
    (sb, ss) = (0, 0)
    for i in range(len(s)):
        preb.append(sb + b[i])
        sb += b[i]
        pres.append(ss + s[i])
        ss += s[i]
    (ptsb, ptss) = ([], [])
    for i in range(len(pres)):
        rem = k - (i + 1)
        ptsb.append(preb[i] + rem * b[i])
        ptss.append(pres[i] + rem * s[i])
    (maxs, maxb) = (max(ptss), max(ptsb))
    if maxs > maxb:
        print('Sasha')
    elif maxs < maxb:
        print('Bodya')
    else:
        print('Draw')