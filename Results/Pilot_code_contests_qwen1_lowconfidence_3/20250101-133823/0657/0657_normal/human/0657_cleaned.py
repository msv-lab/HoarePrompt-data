"""
Author    : raj1307 - Raj Singh
Institute : Jalpaiguri Government Engineering College
Date      : 29.04.19
"""
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
else:
    from builtins import str as __str__
    str = lambda x=b'': x if type(x) is bytes else __str__(x).encode()
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._buffer = BytesIO()
        self._fd = file.fileno()
        self._writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self._buffer.write if self._writable else None

    def read(self):
        return self._buffer.read() if self._buffer.tell() else os.read(self._fd, os.fstat(self._fd).st_size)

    def readline(self):
        while self.newlines == 0:
            (b, ptr) = (os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE)), self._buffer.tell())
            (self._buffer.seek(0, 2), self._buffer.write(b), self._buffer.seek(ptr))
            self.newlines += b.count(b'\n') + (not b)
        self.newlines -= 1
        return self._buffer.readline()

    def flush(self):
        if self._writable:
            os.write(self._fd, self._buffer.getvalue())
            (self._buffer.truncate(0), self._buffer.seek(0))
(sys.stdin, sys.stdout) = (FastIO(sys.stdin), FastIO(sys.stdout))
input = lambda : sys.stdin.readline().rstrip(b'\r\n')

def func_1(*args, **kwargs):
    (sep, file) = (kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout))
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False):
        file.flush()

def func_2():
    return int(input())

def func_3():
    return str(input())

def func_4():
    return map(int, input().strip().split(' '))

def func_5():
    return list(func_4())
abc = 'abcdefghijklmnopqrstuvwxyz'
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod = 1000000007

def func_6(item):
    return item[0]

def func_7(l):
    return sorted(l, key=getKey)

def func_8(n, m, num):
    return [[num for x in range(m)] for y in range(n)]

def func_9(x):
    return x and (not x & x - 1)

def func_10(n):
    return bin(n).replace('0b', '')

def func_11(n):
    return [int(i) for i in str(n)]

def func_12(x, y, p):
    res = 1
    x %= p
    while y > 0:
        if y & 1:
            res = res * x % p
        y = y >> 1
        x = x * x % p1
    return res

def func_13(x, y):
    while y:
        (x, y) = (y, x % y)
    return x

def func_14():
    n = func_2()
    l = func_5()
    a = [1, 1, 1, 2] * 50000
    s = []
    one = l.count(1)
    two = l.count(2)
    'if two==one:\n        for i in range(n):\n            if i%2==0:\n                s.append(2)\n            else:\n                s.append(1)\n        print(*s)\n        exit()\n        \n    \n    for i in range(n):\n        if a[i]==1:\n            if one !=0:\n                s.append(1)\n                one-=1\n            else:\n                s.append(2)\n                two-=1\n        else:\n            if two!=0:\n                s.append(2)\n                two-=1\n            else:\n                s.append(1)\n                one-=1\n    print(*s)   '
    s = [2]
    p = [2]
    two -= 1
    for i in range(1, n):
        if p[-1] % 2 == 0:
            if one != 0:
                s.append(1)
                p.append(p[-1] + 1)
                one -= 1
            else:
                s.append(2)
                p.append(p[-1] + 2)
                two -= 1
        elif two != 0:
            s.append(2)
            p.append(p[-1] + 2)
            two -= 1
        else:
            s.append(1)
            p.append(p[-1] + 1)
            one -= 1
    func_1(*s)
if __name__ == '__main__':
    func_14()