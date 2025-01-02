n = int(raw_input())
s = sorted(map(int, raw_input().split()))
r = 0
for i in xrange(n):
    r += s[i] * (2 ** (n - 1 - i) - 1 - (2 ** i - 1)) % (1000000000 + 7)
print - r