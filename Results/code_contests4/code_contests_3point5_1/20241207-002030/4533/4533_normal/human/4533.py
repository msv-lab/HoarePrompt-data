import sys

n = int(sys.stdin.next())
floors = map(int, sys.stdin.next().split(' '))

m = 0
s = []
for h in floors[::-1]:
    s.append('%i' % ((m - h + 1) if (m - h + 1) > 0 else 0))
    m = max(h, m)

print(' '.join(s[::-1]).strip())
