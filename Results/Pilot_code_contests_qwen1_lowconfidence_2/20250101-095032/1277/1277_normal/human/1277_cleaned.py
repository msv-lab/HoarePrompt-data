"""
// Author : snape_here - Susanta Mukherjee
     
 """
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

def func_1():
    return int(input())

def func_2():
    return float(input())

def func_3():
    return input()

def func_4():
    return map(str, input().split())

def func_5():
    return map(int, input().split())

def func_6():
    return list(func_5())

def func_7():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def func_8(x, y):
    while y:
        (x, y) = (y, x % y)
    return x

def func_9(x, y):
    return x * y // func_8(x, y)
mod = 1000000007

def func_10(b, m):
    g = func_8(b, m)
    if g != 1:
        return -1
    else:
        return pow(b, m - 2, m)

def func_11(a, b, m):
    a = a % m
    inv = func_10(b, m)
    if inv == -1:
        return -999999999
    else:
        return inv * a % m
getcontext().prec = 25
abc = 'abcdefghijklmnopqrstuvwxyz'
pi = 3.141592653589793

def func_12():
    n = func_1()
    a = func_6()
    b = func_6()
    l = [0] * n
    for i in range(n):
        if b[i] > 0:
            l[b[i] - 1] += a[i]
    l1 = []
    for i in range(n):
        l1.append([l[i], i])
    l1.sort()
    ans = 0
    l2 = []
    for i in range(n):
        l2.append(l1[i][1] + 1)
        if b[l1[i][1]] > 0:
            ans += a[l1[i][1]]
        a[l1[i][1]] += l1[i][0]
    func_13(ans)
    func_13(*l2)
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def func_7(self):
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

def func_13(*args, **kwargs):
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
    func_12()