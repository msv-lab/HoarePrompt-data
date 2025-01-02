"""Template for Python Competitive Programmers prepared by Mayank Chaudhary """
'value of mod'
MOD = 998244353
mod = 10 ** 9 + 7
'use resource'
'for factorial'
'uncomment next 4 lines while doing recursion based question'
threading.stack_size(2 ** 27)
sys.setrecursionlimit(10000)
'uncomment modules according to your need'
'\ndef modinv(n, p):\n    return pow(n, p - 2, p)\n'

def func_1():
    return map(int, sys.stdin.readline().strip().split())

def func_2():
    return list(map(int, sys.stdin.readline().strip().split()))

def func_3():
    return sys.stdin.readline().strip()
'*******************************************************'

def func_4():

    def dfs(i):
        if i not in visited:
            visited.add(i)
            for child in mydict_x[i[0]]:
                if (i[0], child) not in visited:
                    dfs((i[0], child))
            for child in mydict_y[i[1]]:
                if (child, i[1]) not in visited:
                    dfs((child, i[1]))
    n = int(func_3())
    lst = []
    count_of_components = 0
    mydict_x = {i: [] for i in range(1, 1001)}
    mydict_y = {i: [] for i in range(1, 1001)}
    for i in range(n):
        (x, y) = func_1()
        lst.append((x, y))
        mydict_x[x].append(y)
        mydict_y[y].append(x)
    visited = set()
    for i in lst:
        if i not in visited:
            dfs(i)
            count_of_components += 1
    print(count_of_components - 1)
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
    threading.Thread(target=main).start()