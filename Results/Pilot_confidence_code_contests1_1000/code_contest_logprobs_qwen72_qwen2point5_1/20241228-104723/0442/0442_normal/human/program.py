from sys import stdin, stdout
from itertools import repeat
def main():
    n = int(stdin.readline())
    dat = map(int, stdin.read().split(), repeat(10, 2 * n - 2))
    d = [0] * n
    p = [-1] * n
    for i in xrange(n - 1):
        x, y = dat[i*2] - 1, dat[i*2+1] - 1
        d[x] += 1
        d[y] += 1
        p[x] = p[y] = i
    c = 0
    a = [-1] * (n - 1)
    for i in xrange(n):
        if d[i] == 1:
            a[p[i]] = c
            c += 1
    for i in xrange(n - 1):
        if a[i] == -1:
            a[i] = c
            c += 1
    stdout.write('\n'.join(map(str, a)))
main()
