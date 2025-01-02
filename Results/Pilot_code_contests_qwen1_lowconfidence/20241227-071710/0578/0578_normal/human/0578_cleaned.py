inf = float('inf')
mod = int(1000000000.0) + 7
mod_ = 998244353

def func_1():
    (n, k) = map(int, func_5().split())
    s = func_5()
    t = func_5()
    freq = Counter(s)
    groups = [m.group(0) for m in re.finditer('([a-z])\\1*', t)]
    for group in groups:
        div = len(group) // k
        rem = len(group) % k
        if freq[group[0]] < rem:
            func_3('No')
            return
        freq[group[0]] -= rem
        if div == 0:
            continue
        for i in range(string.ascii_lowercase.index(group[0]) - 1, -1, -1):
            if freq[string.ascii_lowercase[i]] >= div:
                freq[string.ascii_lowercase[i]] -= div
                break
        else:
            func_3('No')
            return
    func_3('Yes')

def func_2():
    for _ in range(int(func_5())):
        func_1()
BUFSIZE = 8192

class FastI(IOBase):

    def __init__(self, file):
        self._fd = file.fileno()
        self._buffer = StringIO()
        self.newlines = 0

    def read(self):
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
            self.newlines = b.count('\n') + (not b)
            ptr = self._buffer.tell()
            (self._buffer.seek(0, 2), self._buffer.write(b), self._buffer.seek(ptr))
        self.newlines -= 1
        return self._buffer.readline()

class FastO(IOBase):

    def __init__(self, file):
        self._fd = file.fileno()
        self._buffer = __pypy__.builders.StringBuilder()
        self.write = lambda s: self._buffer.append(s)

    def flush(self):
        os.write(self._fd, self._buffer.build())
        self._buffer = __pypy__.builders.StringBuilder()

def func_3(*args, **kwargs):
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

def func_4(x, y):
    while y:
        (x, y) = (y, x % y)
    return x
(sys.stdin, sys.stdout) = (FastI(sys.stdin), FastO(sys.stdout))

def func_5():
    return sys.stdin.readline().rstrip('\r\n')
if __name__ == '__main__':

    def bootstrap(cont):
        (call, arg) = cont.switch()
        while True:
            (call, arg) = cont.switch(to=continulet(lambda _, f, args: f(*args), call, arg))
    cont = continulet(bootstrap)
    cont.switch()
    func_2()