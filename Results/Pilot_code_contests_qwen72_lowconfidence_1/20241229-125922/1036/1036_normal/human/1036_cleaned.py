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
    return map(str, input().strip().split(' '))

def func_5():
    return list(func_3())

def func_6():
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

def func_7(item):
    return item[1]

def func_8(l):
    return sorted(l, key=getKey, reverse=True)

def func_9(n, m, num):
    return [[num for x in range(m)] for y in range(n)]

def func_10(x):
    return x and (not x & x - 1)

def func_11(n):
    return bin(n).replace('0b', '')

def func_12(n):
    return [int(i) for i in str(n)]

def func_13(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def func_14(x, y, p):
    res = 1
    x %= p
    while y > 0:
        if y & 1:
            res = res * x % p
        y = y >> 1
        x = x * x % p
    return res

def func_15(x, y):
    while y:
        (x, y) = (y, x % y)
    return x

def func_16(n):
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

def func_17():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def func_18():
    if True:
        (n, m, k) = func_3()
        a = func_5()
        b = func_5()
        x = [0] * (n + 5)
        y = [0] * (m + 5)
        x[0] = a[0]
        fx = {}
        p = []
        q = []
        if x[0] == 1:
            fx[1] = 1
            p.append(1)
        for i in range(1, n):
            if a[i] != 0:
                x[i] += x[i - 1] + a[i]
                if fx.get(x[i], 0) == 0:
                    fx[x[i]] = 1
                else:
                    fx[x[i]] += 1
                p.append(x[i])
            else:
                x[i] = 0
        y[0] = b[0]
        fy = {}
        if y[0] == 1:
            fy[1] = 1
            q.append(1)
        for i in range(1, m):
            if b[i] != 0:
                y[i] += y[i - 1] + b[i]
                if fy.get(y[i], 0) == 0:
                    fy[y[i]] = 1
                else:
                    fy[y[i]] += 1
                q.append(y[i])
            else:
                y[i] = 0
        p = list(set(p))
        q = list(set(q))
        cnt = 0
        for i in range(len(p) - 1, -1, -1):
            fx[p[i]] = fx[p[i]] + cnt
            cnt = fx[p[i]]
        cnt = 0
        for i in range(len(q) - 1, -1, -1):
            fy[q[i]] = fy[q[i]] + cnt
            cnt = fy[q[i]]
        ans = 0
        for i in p:
            if k & i != 0:
                continue
            if fx.get(i, 0) == 0 or fy.get(k // i, 0) == 0:
                continue
            if k % i == 0:
                ans += fx[i] * fy[k // i]
        func_19(ans)
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def func_17(self):
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