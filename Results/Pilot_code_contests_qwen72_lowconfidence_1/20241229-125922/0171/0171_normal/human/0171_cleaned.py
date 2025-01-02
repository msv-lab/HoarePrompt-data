input = sys.stdin.readline
for _ in xrange(int(input())):
    n = int(input())
    seq = [int(x) for x in input().split()]
    s = sorted([i + seq[i % n] for i in xrange(2 * n)])
    ans = 'YES'
    for i in xrange(1, len(s)):
        if s[i] == s[i - 1]:
            ans = 'NO'
            break
    print(ans)