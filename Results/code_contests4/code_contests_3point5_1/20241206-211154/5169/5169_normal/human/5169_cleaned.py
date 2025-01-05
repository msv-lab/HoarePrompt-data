"""Uncomment modules according to your need"""
if sys.version_info[0] < 3:
    input = raw_input
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
'value of mod'
MOD = 998244353
mod = 10 ** 9 + 7
'Uncomment next 4 lines if doing huge recursion'

def func_1(mod=mod):
    """ returns two lists, factorial and inverse factorial modulo argument by default 10**9 +7 """
    fact = [1]
    for i in range(1, 200005):
        fact.append(fact[-1] * i % mod)
    ifact = [0] * 200005
    ifact[200004] = pow(fact[200004], mod - 2, mod)
    for i in range(200004, 0, -1):
        ifact[i - 1] = i * ifact[i] % mod
    return (fact, ifact)

def func_2(n, p):
    """ returns N inverse modulo p """
    return pow(n, p - 2, p)

def func_3(n, r, fact, ifact):
    """ takes 4 arguments: n , r and factorial and inverse factorial lists"""
    t = fact[n] * (ifact[r] * ifact[n - r]) % MOD % MOD
    return t

def func_4(Sum):
    """this function returns the maximum n for which Summation(n) <= Sum"""
    ans = (-1 + sqrt(1 + 8 * Sum)) // 2
    return ans

def func_5(n):
    """ returns a list of prime numbers till n """
    if n < 2:
        return list()
    prime = [True for _ in range(n + 1)]
    p = 3
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 2
    r = [2]
    for p in range(3, n + 1, 2):
        if prime[p]:
            r.append(p)
    return r

def func_6(n, start=1):
    """ returns a list of all divisors till n """
    divisors = []
    for i in range(start, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors.extend([i, n // i])
    return divisors

def func_7(n, primes):
    """ returns the number of divisors, two arguments n and the sieve till n """
    divs_number = 1
    for i in primes:
        if n == 1:
            return divs_number
        t = 1
        while n % i == 0:
            t += 1
            n //= i
        divs_number *= t

def func_8(d, x, default=-1):
    """ Takes 2 arguments an iterable and an element. returns a tuple (firstoccurence,lastoccurence) -1 if not found """
    left = right = -1
    for i in range(len(d)):
        if d[i] == x:
            if left == -1:
                left = i
            right = i
    if left == -1:
        return (default, default)
    else:
        return (left, right)

def func_9(x, y):
    """ returns greatest common divisor of x and y """
    while y:
        (x, y) = (y, x % y)
    return x

def func_10(a):
    """ returns True/False """
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

def func_11(n, k=1):
    return n // k + (n % k != 0)

def func_12():
    return sys.stdin.readline().strip()

def func_13():
    return int(func_12())

def func_14():
    return map(int, func_12().split())

def func_15():
    return list(map(int, func_12().split()))

def func_16():
    return func_12().split()

def func_17(a, b):
    return abs(a * b) // func_9(a, b)

def func_18(a, sep=' ', end='\n'):
    print(sep.join(map(str, a)), end=end)

def func_19():
    return defaultdict(int)

def func_20():
    return defaultdict(list)

def func_21(s):
    return sys.stdout.write(s)

def func_22():
    (n, m, k) = func_14()
    a = func_15()
    b = func_15()
    ptr1 = 0
    ptr2 = 0
    totaltime = 0
    check = True
    count = 0
    while ptr1 < n and ptr2 < m:
        if a[ptr1] < b[ptr2]:
            if totaltime + a[ptr1] <= k:
                totaltime += a[ptr1]
                count += 1
                ptr1 += 1
            else:
                check = False
                break
        elif totaltime + b[ptr2] <= k:
            totaltime += b[ptr2]
            count += 1
            ptr2 += 1
        else:
            check = False
            break
    if check == False:
        print(count)
    else:
        while ptr1 < n:
            if totaltime + a[ptr1] <= k:
                totaltime += a[ptr1]
                count += 1
                ptr1 += 1
            else:
                check = False
                break
        while ptr2 < m:
            if totaltime + b[ptr2] <= k:
                totaltime += b[ptr2]
                count += 1
                ptr2 += 1
            else:
                check = False
                break
        print(count)
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
    func_22()