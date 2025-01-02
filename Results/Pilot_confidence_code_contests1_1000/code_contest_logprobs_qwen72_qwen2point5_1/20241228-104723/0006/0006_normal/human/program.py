from sys import stdout
def solve():
    n, l, r = map(int, raw_input().split())
    l -= 1
    for i in xrange(n - 1):
        t = (n - i - 1) * 2
        if l < t:
            break
        l -= t
        r -= t
    else:
        stdout.write('1\n')
        return
    ans = [0] * (r - l)
    i += 1
    p = i + 1
    sw = 0
    for j in xrange(r):
        if sw:
            if j >= l:
                ans[j-l] = p
            p += 1
            if p > n:
                i += 1
                p = i + 1
                if i == n:
                    i = 1
        else:
            if j >= l:
                ans[j-l] = i
        sw = 1 - sw
    stdout.write(' '.join(map(str, ans)))
    stdout.write('\n')

T = int(raw_input())
for _ in xrange(T):
    solve()
