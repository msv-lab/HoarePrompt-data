inf = float('inf')
mod_ = int(1000000000.0) + 7
mod = 998244353

def func_1(n):
    from functools import reduce
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

def func_2(n):
    arr = [1] * n
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i] == 1:
            for j in range(i, n, i):
                arr[j] = i
    return arr

def func_3(arr, k):
    for i in range(len(arr)):
        if arr[i] != '?':
            for j in range(i, len(arr), k):
                if arr[j] != arr[i] and arr[j] != '?':
                    return False
                if arr[j] == '?':
                    arr[j] = arr[i]
        else:
            vis = set([])
            for j in range(i, len(arr), k):
                if arr[j] != '?':
                    vis.add(arr[j])
            if len(vis) == 2:
                return False
            if len(vis) == 1:
                put = list(vis)[0]
                for j in range(i, len(arr), k):
                    arr[j] = put
    dic = {'1': 0, '0': 0, '?': 0}
    for i in range(k):
        dic[arr[i]] += 1
    if dic['1'] != dic['0'] and dic['?'] != abs(dic['1'] - dic['0']):
        return False
    return True

def func_4():
    for _ in range(int(input())):
        (n, k) = map(int, input().split())
        arr = list(input())
        if not func_3(arr, k):
            func_5('NO')
        else:
            func_5('YES')
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

def func_5(*args, **kwargs):
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

def func_6(x, y):
    while y:
        (x, y) = (y, x % y)
    return x
(sys.stdin, sys.stdout) = (FastI(sys.stdin), FastO(sys.stdout))
input = lambda : sys.stdin.readline().rstrip('\r\n')
if __name__ == '__main__':
    func_4()