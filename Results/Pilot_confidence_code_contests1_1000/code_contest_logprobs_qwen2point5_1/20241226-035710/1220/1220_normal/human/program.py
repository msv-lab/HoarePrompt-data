from sys import stdin, stdout
from itertools import repeat
def main():
    n, k = map(int, stdin.readline().split())
    a = map(int, stdin.readline().split(), repeat(10, k))
    l = range(1, n + 1)
    d = [0] * (n + 1)
    s = []
    b = []
    for x in a:
        while s and s[-1] < x:
            b.append(s.pop())
        s.append(x)
        d[x] = 1
    if b != range(1, len(b) + 1):
        print -1
        return
    l = 0
    while s:
        x = y = s.pop() - 1
        while x > l:
            if not d[x]:
                a.append(x)
            x -= 1
        l = y + 1
    for i in xrange(n, l, -1):
        a.append(i)
    stdout.write(' '.join(map(str, a)))
main()
