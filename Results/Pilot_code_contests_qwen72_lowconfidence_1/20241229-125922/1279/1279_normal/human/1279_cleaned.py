inf = float('inf')
mod = int(1000000000.0) + 7
mod_ = 998244353

def func_1(n):
    from functools import reduce
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

def func_2(n):
    arr = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, n, i):
                arr[j] = False
    primes = []
    for i in range(n):
        if arr[i]:
            primes.append(i)
    return primes

def func_3():

    def cost(arr):
        cst = 0
        for i in range(len(arr) - 1, 0, -1):
            cst += abs(arr[i] - arr[i - 1])
        return cst
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        temp = list(arr)
        temp[0] = temp[1]
        cost1 = cost(temp)
        temp = list(arr)
        temp[1] = temp[0]
        cost1 = min(cost1, cost(temp))
        temp = list(arr)
        temp[-2] = temp[-1]
        cost1 = min(cost1, cost(temp))
        temp = list(arr)
        temp[-1] = temp[-2]
        cost1 = min(cost1, cost(temp))
        func_4(cost1)
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

def func_4(*args, **kwargs):
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

def func_5(x, y):
    while y:
        (x, y) = (y, x % y)
    return x
(sys.stdin, sys.stdout) = (FastI(sys.stdin), FastO(sys.stdout))
input = lambda : sys.stdin.readline().rstrip('\r\n')
if __name__ == '__main__':
    func_3()