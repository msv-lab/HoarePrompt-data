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

def func_1(a, k):
    (bags, carry) = (0, 0)
    for i in a:
        if carry != 0:
            bags += 1
            i = max(0, i - carry)
        bags += i // k
        carry = i % k
    if carry != 0:
        bags += 1
    return bags

def func_2():
    (_, k) = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    print(min(func_1(a, k), func_1(a[::-1], k)))
if __name__ == '__main__':
    func_2()