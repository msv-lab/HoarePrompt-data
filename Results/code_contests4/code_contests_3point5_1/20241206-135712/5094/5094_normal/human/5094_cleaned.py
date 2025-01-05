"""
What I cannot create, I do not understand.

https://github.com/Cheran-Senthil/PyRival
Copyright (c) 2018 Cheran Senthilkumar
"""

class dict(dict):

    def items(self):
        return dict.iteritems(self)

    def keys(self):
        return dict.iterkeys(self)

    def values(self):
        return dict.itervalues(self)
filter = itertools.ifilter
map = itertools.imap
zip = itertools.izip
input = raw_input
range = xrange
MOD = 1000000007
INF = float('+inf')
ASCII_LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
ASCII_UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def func_1():
    (n, k) = map(int, input().split(' '))
    h = Counter(map(int, input().split(' ')))
    (tot, cnt) = (0, 0)
    slices = 0
    for i in range(200000, min(h) - 1, -1):
        if i in h:
            tot += h[i]
        if cnt + tot > k:
            cnt = tot
            slices += 1
        else:
            cnt += tot
    print(slices)
if __name__ == '__main__':
    func_1()