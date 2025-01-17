def getsubarray(a):
    res = []
    for i in range(len(a)):
        total = 0
        for j in range(i, len(a)):
            total += a[j]
            res.append(total)
    res.sort()
    return res

def getodd(a):
    res = []
    for e in a:
        if res and e == res[-1]:
            res.pop()
        else:
            res.append(e)
    return res

def getpalindrome(odds, n):
    res = [0] * n
    pre = 0
    idx = (n - 1) // 2
    for e in odds:
        if idx == n - 1 - idx:
            res[idx] = e
        else:
            res[idx] = (e - pre) // 2
            res[n - 1 - idx] = (e - pre) // 2
        pre = e
        idx -= 1
    return res

def getlargest(lhs, rhs):
    while rhs and lhs[-1] == rhs[-1]:
        lhs.pop()
        rhs.pop()
    return lhs[-1]

def solve():
    n = int(input())
    s = list(map(int, input().split()))

    s.sort()
    odds = getodd(s)

    miss = -1
    if len(odds) > (n + 1) // 2:
        odd = []
        even = []
        for e in odds:
            if e % 2:
                odd.append(e)
            else:
                even.append(e)

        if odd and even:
            miss = even[0] if len(even) == 1 else odd[0]
        else:
            b = getpalindrome(odds, n + 2)
            bsum = getsubarray(b)
            y = bsum[-1]
            x = getlargest(bsum, s)
            miss = 2 * x - y
    else:
        b = getpalindrome(odds, n - 2)
        bsum = getsubarray(b)
        y = bsum[-1]
        x = getlargest(s, bsum)
        miss = 2 * x - y

    odds.append(miss)
    odds.sort()
    odds = getodd(odds)

    ans = getpalindrome(odds, n)
    print(*ans)

T = 1
if True:
    T = int(input())
for _ in range(T):
    solve()
