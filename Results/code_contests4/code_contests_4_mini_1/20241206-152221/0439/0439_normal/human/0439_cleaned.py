transpose = lambda mat: [''.join(col) for col in zip(*mat)]

def func_1(n, m, grid):

    def get_adj(i, j):
        adj = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
        res = []
        for (ai, aj) in adj:
            if 0 <= ai < n and 0 <= aj < m and (grid[ai][aj] == '#'):
                res.append((ai, aj))
        return res
    (components, visited) = (0, [[False] * m for _ in range(n)])

    def dfs(i, j):
        (component, stack) = (1, [(i, j)])
        while stack:
            (si, sj) = stack[-1]
            if visited[si][sj]:
                stack.pop()
                continue
            else:
                visited[si][sj] = True
                component = 1
                for (ai, aj) in get_adj(si, sj):
                    if not visited[ai][aj]:
                        stack.append((ai, aj))
        return component
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == '#':
                components += dfs(i, j)
    return components

def func_2():
    (n, m) = map(int, input().split())
    grid = [input() for _ in range(n)]
    if grid == ['.' * m for _ in range(n)]:
        func_3(0)
        return
    for row in grid:
        (start, stop) = (row.find('#'), row.rfind('#'))
        if start == -1 or '.' in row[start:stop + 1]:
            func_3(-1)
            return
    grit = transpose(grid)
    for row in grit:
        (start, stop) = (row.find('#'), row.rfind('#'))
        if start == -1 or '.' in row[start:stop + 1]:
            func_3(-1)
            return
    func_3(func_1(n, m, grid))
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
(sys.stdin, sys.stdout) = (FastI(sys.stdin), FastO(sys.stdout))
input = lambda : sys.stdin.readline().rstrip('\r\n')
if __name__ == '__main__':
    func_2()