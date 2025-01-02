if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

class DisjointSetUnion:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            (self.parent[acopy], acopy) = (a, self.parent[acopy])
        return a

    def union(self, a, b):
        (a, b) = (self.find(a), self.find(b))
        if a != b:
            if self.size[a] < self.size[b]:
                (a, b) = (b, a)
            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

def func_1():
    (n, m) = map(int, input().split())
    dsu = DisjointSetUnion(n * m)
    f_col = [-1] * n
    f_row = [-1] * m
    cols = set(range(n))
    rows = set(range(m))
    exists = True
    black = False
    white = 0
    prev_row = '.' * m
    for i in range(n):
        row = input()
        for j in range(m):
            if row[j] == prev_row[j] == '#':
                dsu.union(i * m + j, (i - 1) * m + j)
            if j and row[j] == row[j - 1] == '#':
                dsu.union(i * m + j, i * m + j - 1)
            if row[j] == '#':
                black = True
                f_col[i] = f_col[i] if f_col[i] != -1 else j
                f_row[j] = f_row[j] if f_row[j] != -1 else i
                exists &= abs(f_col[i] - j) < 2
                exists &= abs(f_row[j] - i) < 2
                f_col[i] = j
                f_row[j] = i
                cols.discard(i)
                rows.discard(j)
            else:
                white += 1
        prev_row = row
    if (not cols and (not rows) or not black) and exists:
        func_2(len(dsu) - white)
    else:
        func_2(-1)
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

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

def func_2(*args, **kwargs):
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
    func_1()