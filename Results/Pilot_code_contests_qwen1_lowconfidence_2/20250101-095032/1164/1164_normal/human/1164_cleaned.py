sys.setrecursionlimit(10 ** 4)
i_m = 9223372036854775807

def func_1(n, p):
    return pow(n, p - 2, p)

def func_2():
    return map(int, func_4().split())

def func_3():
    return list(map(int, func_4().split()))

def func_4():
    return input()

def func_5():
    return int(input())

def func_6(x, y):
    x = abs(x)
    y = abs(y)
    if min(x, y) == 0:
        return max(x, y)
    while y:
        (x, y) = (y, x % y)
    return x

def func_7(n):
    l = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if n // i == i:
                l.append(i)
            else:
                l.append(i)
                l.append(n // i)
    return l
prime = []

def func_8(n):
    global prime
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    f = []
    for p in range(2, n):
        if prime[p]:
            f.append(p)
    return f

def func_9(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            a.append(i)
            n = n // i
    if n > 2:
        a.append(n)
    return a
'*******************************************************'

def func_10():
    n = func_5()
    a = func_3()
    d = []
    p = 0
    for i in range(0, n - 1):
        d.append(a[i + 1] - a[i])
        p += max(a[i + 1] - a[i], 0)
    print((a[0] - p + 1) // 2 + p)
    t = func_5()
    for _ in range(t):
        (l, r, x) = func_2()
        l -= 1
        r -= 1
        if l == 0:
            a[0] += x
        if l > 0:
            p -= max(0, d[l - 1])
            d[l - 1] += x
            p += max(0, d[l - 1])
        if r < n - 1:
            p -= max(0, d[r])
            d[r] -= x
            p += max(0, d[r])
        print((a[0] - p + 1) // 2 + p)
py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange
BUFSIZE = 8192

class FastIO(BytesIO):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.writable = 'x' in file.mode or 'w' in file.mode
        self.write = super(FastIO, self).write if self.writable else None

    def _fill(self):
        s = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
        self.seek((self.tell(), self.seek(0, 2), super(FastIO, self).write(s))[0])
        return s

    def read(self):
        while self._fill():
            pass
        return super(FastIO, self).read()

    def readline(self):
        while self.newlines == 0:
            s = self._fill()
            self.newlines = s.count(b'\n') + (not s)
        self.newlines -= 1
        return super(FastIO, self).readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.getvalue())
            (self.truncate(0), self.seek(0))

class IOWrapper(IOBase):

    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        if py2:
            self.write = self.buffer.write
            self.read = self.buffer.read
            self.readline = self.buffer.readline
        else:
            self.write = lambda s: self.buffer.write(s.encode('ascii'))
            self.read = lambda : self.buffer.read().decode('ascii')
            self.readline = lambda : self.buffer.readline().decode('ascii')
(sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))
input = lambda : sys.stdin.readline().rstrip('\r\n')

class ostream:

    def __lshift__(self, a):
        sys.stdout.write(str(a))
        return self
cout = ostream()
endl = '\n'

def func_11(zero=0):
    conv = ord if py2 else lambda x: x
    A = []
    numb = zero
    sign = 1
    i = 0
    s = sys.stdin.buffer.read()
    try:
        while True:
            if s[i] >= b'R'[0]:
                numb = 10 * numb + conv(s[i]) - 48
            elif s[i] == b'-'[0]:
                sign = -1
            elif s[i] != b'\r'[0]:
                A.append(sign * numb)
                numb = zero
                sign = 1
            i += 1
    except:
        pass
    if s and s[-1] >= b'R'[0]:
        A.append(sign * numb)
    return A
if __name__ == '__main__':
    func_10()