import sys

t = int(sys.stdin.readline())
for i in xrange(t):
    a, b, c = map(int, sys.stdin.readline().split())

    k2 = min(b / 1, c / 2)

    b -= 1 * k2
    c -= 2 * k2

    k1 = min(a / 1, b / 2)
    a -= 1 * k1
    b -= 2 * k1

    print (k1 + k2) * 3
