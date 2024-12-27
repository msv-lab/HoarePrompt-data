n, a, s, j = input(), map(int, raw_input().split()), 0, 0
for i in xrange(n-1):
    if a[i] > a[i+1]:
        s, j = s+1, n-i-1
        if s > 1:
            print -1
            break
else:
    print -1 if s and a[-1] > a[0] else j