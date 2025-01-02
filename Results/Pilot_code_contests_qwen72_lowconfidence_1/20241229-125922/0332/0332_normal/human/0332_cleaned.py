rstr = lambda : stdin.readline().strip()
(s, t) = (sorted(rstr()), sorted(rstr(), reverse=True))
le = len(s)
if le == 1:
    print(s[0])
elif le == 2:
    print(min(s[0] + t[0], t[0] + s[0]))
elif s[0] <= t[0]:
    ans = []
    for i in range(le):
        ans.append(t[i >> 1] if i & 1 else s[i >> 1])
    if le & 1 and ans[-1] > ans[-2]:
        (ans[-1], ans[-2]) = (ans[-2], ans[-1])
    print(''.join(ans))
else:
    (mds, mdt, ans) = (int(ceil(le / 2)) - 1, (le >> 1) - 1, [])
    for i in range(le):
        if i & 1:
            ans.append(t[mdt])
            mdt -= 1
        else:
            ans.append(s[mds])
            mds -= 1
    print(''.join(ans[::-1]))