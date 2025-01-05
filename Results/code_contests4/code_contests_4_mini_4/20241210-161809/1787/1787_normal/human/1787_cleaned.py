"""Template for Python Competitive Programmers prepared by pa.n.ik, kabeer seth and Mayank Chaudhary """
'value of mod'
MOD = 998244353
mod = 10 ** 9 + 7
'use resource'
'for factorial'

def func_1():
    fact = [1]
    for i in range(1, 100005):
        fact.append(fact[-1] * i % mod)
    ifact = [0] * 100005
    ifact[100004] = pow(fact[100004], mod - 2, mod)
    for i in range(100004, 0, -1):
        ifact[i - 1] = i * ifact[i] % mod
    return (fact, ifact)
'uncomment next 4 lines while doing recursion based question'
'uncomment modules according to your need'

def func_2(n, p):
    return pow(n, p - 2, p)

def func_3(n, r, fact, ifact):
    t = fact[n] * (ifact[r] * ifact[n - r]) % mod % mod
    return t

def func_4():
    return map(int, sys.stdin.readline().strip().split())

def func_5():
    return list(map(int, sys.stdin.readline().strip().split()))

def func_6():
    return sys.stdin.readline().strip()
'*****************************************************************************************'

def func_7(x, y):
    while y:
        (x, y) = (y, x % y)
    return x

def func_8(x, y):
    return x * y // func_7(x, y)

def func_9(n):
    return [n, 1, n + 1, 0][n % 4]

def func_10(a, b):
    res = 1
    while b:
        if b & 1:
            res = res * a
            res %= MOD
            b -= 1
        else:
            a = a * a
            a %= MOD
            b >>= 1
    res %= MOD
    return res

def func_11(P):
    ans = (-1 + sqrt(1 + 8 * P)) // 2
    return ans
' ********************************************************************************************* '

def func_12():
    T = int(func_6())
    while T:
        n = int(func_6())
        Arr = func_5()
        p = Arr[0]
        flag = 0
        for i in Arr[1:]:
            if i != p:
                flag = 1
                break
        if flag == 1:
            print(1)
        else:
            print(n)
        T -= 1
' -------- Python 2 and 3 footer by Pajenegod and c1729 ---------'
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
' main function'
if __name__ == '__main__':
    func_12()