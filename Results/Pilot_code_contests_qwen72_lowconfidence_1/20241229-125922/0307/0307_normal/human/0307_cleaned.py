"""                         
Beautiful is better than ugly.
    Explicit is better than implicit.
Simple is better than complex.
    Complex is better than complicated.
Flat is better than nested.
    Sparse is better than dense.
                    
    * Readability counts *

 // Author : raj1307 - Raj Singh
 // Date   : 7.07.19

"""
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
else:
    _str = str
    str = lambda x=b'': x if type(x) is bytes else _str(x).encode()

def func_1():
    return int(input())

def func_2():
    return input()

def func_3():
    return map(int, input().strip().split(' '))

def func_4():
    return list(func_3())

def func_5():
    sys.setrecursionlimit(100000000)
    threading.stack_size(40960000)
    thread = threading.Thread(target=main)
    thread.start()
abc = 'abcdefghijklmnopqrstuvwxyz'
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
(mod, MOD) = (1000000007, 998244353)
vow = ['a', 'e', 'i', 'o', 'u']
(dx, dy) = ([-1, 1, 0, 0], [0, 0, 1, -1])

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
    return [i for i in str(n)]

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

def func_14(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def func_15():
    (n, k, m, t) = func_3()
    for i in range(t):
        (a, b) = func_3()
        if a == 1:
            n += 1
            if b <= k:
                k += 1
        elif b < k:
            n -= b
            k -= b
        else:
            n -= n - b
        func_16(n, k)
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        if self.buffer.tell():
            return self.buffer.read()
        return os.read(self._fd, os.fstat(self._fd).st_size)

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            (self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            (self.buffer.truncate(0), self.buffer.seek(0))

def func_16(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
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
(sys.stdin, sys.stdout) = (FastIO(sys.stdin), FastIO(sys.stdout))
input = lambda : sys.stdin.readline().rstrip(b'\r\n')
if __name__ == '__main__':
    func_15()