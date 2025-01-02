if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

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
mod = 1000000007
inf = float('inf')
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
    return [int(i) for i in str(n)]

def func_12(x, y, p):
    res = 1
    x %= p
    while y > 0:
        if y & 1:
            res = res * x % p
        y = y >> 1
        x = x * x % p
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
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def func_16():
    func_19('YES')

def func_17():
    func_19('NO')

def func_18():
    (x1, y1, x2, y2) = func_3()
    (x3, y3, x4, y4) = func_3()
    (x5, y5, x6, y6) = func_3()
    one = two = True
    if x5 > x2 or y6 < y1 or x6 < x1 or (y5 > y2):
        one = False
    if y3 > y2 or y4 < y1 or x3 > x2 or (x4 < x1):
        two = False
    if not one and (not two):
        func_16()
        exit()
    if True:
        y4 = min(y4, y2)
        y3 = max(y3, y1)
        y6 = min(y6, y2)
        y5 = max(y5, y1)
        x4 = min(x4, x2)
        x3 = max(x3, x1)
        x6 = min(x6, x2)
        x5 = max(x5, x1)
        if two and one:
            area = abs(x1 - x2) * abs(y1 - y2)
            a1 = abs(x3 - x4) * abs(y3 - y4)
            a2 = abs(x5 - x6) * abs(y5 - y6)
            if a1 + a2 < area:
                func_16()
            else:
                func_17()
        elif one == True:
            a2 = abs(x5 - x6) * abs(y5 - y6)
            if a2 < area:
                func_16()
            else:
                func_17()
        elif two:
            a1 = abs(x3 - x4) * abs(y3 - y4)
            if a1 < area:
                func_16()
            else:
                func_17()
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def func_15(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            (self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
        self.newlines = 0
        return self.buffer.read()

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

class IOWrapper(IOBase):

    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda : self.buffer.read().decode('ascii')
        self.readline = lambda : self.buffer.readline().decode('ascii')

def func_19(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    (sep, file) = (kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout))
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False):
        file.flush()
if sys.version_info[0] < 3:
    (sys.stdin, sys.stdout) = (FastIO(sys.stdin), FastIO(sys.stdout))
else:
    (sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))
input = lambda : sys.stdin.readline().rstrip('\r\n')
if __name__ == '__main__':
    func_18()