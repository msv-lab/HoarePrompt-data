n = int(raw_input())
a = list(map(int, raw_input().split()))
s = []
for i in a:
    ts = bin(i)[2:]
    ts = ts[::-1]
    while len(ts) < 32:
        ts += '0'
    s.append(ts)
ans = ''
brk = -1
leftp = 0
ansl = -1
ansr = -1
for j in range(31, -1, -1):
    c1 = 0
    c0 = 0
    for i in range(n):
        if s[i][j] == '0':
            c0 += 1
        else:
            c1 += 1
    if c1 == n:
        ans += '1'
    elif c0 == n:
        ans += '0'
    else:
        mx0 = 0
        mx1 = 0
        ans += '1'
        leftp = int(ans, 2)
        leftp <<= j
        for i in range(n):
            if s[i][j] == '0':
                mx0 = max(mx0, int(s[i][:j][::-1], 2))
            else:
                mx1 = max(mx1, int(s[i][:j][::-1], 2))
        ansl = leftp + mx0
        ansr = leftp + mx1
        break
if ansl == -1:
    leftp = int(ans, 2)
    a1 = 0
    for i in a:
        a1 = max(a1, leftp ^ i)
    print(a1)
else:
    m1 = 0
    m0 = 0
    for i in a:
        m1 = max(m1, ansr ^ i)
        m0 = max(m0, ansl ^ i)
    print(min(m1, m0))