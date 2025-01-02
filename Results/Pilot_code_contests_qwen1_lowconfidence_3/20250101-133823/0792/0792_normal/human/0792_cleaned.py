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

def func_8(n):
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
q = []

def func_9(n, d, v, c):
    global q
    v[n] = 1
    x = d[n]
    q.append(n)
    j = c
    for i in x:
        if i not in v:
            f = func_9(i, d, v, c + 1)
            j = max(j, f)
    return j
'*******************************************************'

def func_10():
    (n, m, k) = func_2()
    a = func_3()
    b = [0]
    b.append(a[0])
    if m == 1:
        a.sort(reverse=True)
        print(sum(a[:k]))
        sys.exit()
    for i in range(1, n):
        b.append(a[i] + b[-1])
    d = [[0] * n]
    for i in range(1, k + 1):
        dd = []
        p = 0
        for j in range(n + 1):
            if j < m:
                dd.append(0)
            else:
                f = d[i - 1][j - m] + b[j] - b[j - m]
                p = max(f, p)
                dd.append(p)
        d.append(dd)
    print(max(d[-1]))
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