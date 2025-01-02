def func_1():
    import sys, re, math
    from collections import deque, defaultdict, Counter, OrderedDict
    from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, floor
    from heapq import heappush, heappop, heapify, nlargest, nsmallest

    def STR():
        return list(input())

    def INT():
        return int(input())

    def MAP():
        return map(int, input().split())

    def LIST():
        return list(map(int, input().split()))

    def list2d(a, b, c):
        return [[c] * b for i in range(a)]

    def sortListWithIndex(listOfTuples, idx):
        return sorted(listOfTuples, key=lambda x: x[idx])

    def sortDictWithVal(passedDic):
        temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
        toret = {}
        for tup in temp:
            toret[tup[0]] = tup[1]
        return toret

    def sortDictWithKey(passedDic):
        return dict(OrderedDict(sorted(passedDic.items())))
    INF = float('inf')
    mod = 10 ** 9 + 7
    t = INT()
    while t != 0:
        n = INT()
        zz = []
        for _ in range(n):
            zz.append(LIST())
        prevplay = 0
        prevClr = 0
        flag = 0
        for i in range(n):
            if zz[i][0] < prevplay or zz[i][1] < prevClr or zz[i][0] < zz[i][1]:
                flag = 1
                break
            if zz[i][1] > prevClr:
                temp = zz[i][1] - prevClr
                temp1 = zz[i][0] - prevplay
                if temp > temp1:
                    flag = 1
                    break
            prevplay = zz[i][0]
            prevClr = zz[i][1]
        if flag == 1:
            print('NO')
        else:
            print('YES')
        t -= 1
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

def func_2(zero=0):
    conv = ord if py2 else lambda x: x
    A = []
    numb = zero
    sign = 1
    i = 0
    s = sys.stdin.buffer.read()
    try:
        while True:
            if s[i] >= b'0'[0]:
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
    if s and s[-1] >= b'0'[0]:
        A.append(sign * numb)
    return A
if __name__ == '__main__':
    func_1()