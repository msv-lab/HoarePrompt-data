from __future__ import division, print_function

''' Hey stalker :) '''
INF = 10 ** 10
TEST_CASES = True


def main():
    n, k = get_list()
    li = get_list()
    req = set()
    for i in li:
        r = 0
        #print(i)
        while i>0:
            j = 0
            while i%(k**(j+1))==0: j+=1
            i //= k**j
            j += r
            #print(i, j)
            if j in req:
                print('NO')
                return
            req.add(j)
            r = j
            i -= 1
    print('YES')

class SegTreeSum:
    def __init__(self, size):
        self.n = 1 << size.bit_length()
        self.li = [0]*(self.n<<1)

    def set(self, index, ele):
        index += self.n
        self.li[index] = ele
        while index>1:
            self.li[index>>1] = self.li[index] + self.li[index^1]
            index >>= 1

    def add(self, index, val):
        self.set(index, self.get(index)+val)

    def get(self, index):
        return self.li[self.n + index]

    def query(self, l, r):  # L and R inclusive
        #[print(i, self.li[i]) for i in range(len(self.li))]
        res = 0
        l, r = l+self.n, r+self.n
        while l<=r:
            #print(l, r)
            if l&1==1: res += self.li[l]
            if r&1!=1: res += self.li[r]
            l = (l+1)>>1
            r = (r-1)>>1
        return res

''' FastIO Footer by @c1729 and other contributors '''
import os
import sys
from bisect import bisect_left, bisect_right
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
# else:
#     sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")
get_int = lambda: int(input())
get_list = lambda: list(map(int, input().split()))
if __name__ == "__main__":
    if TEST_CASES:
        [main() for _ in range(int(input()))]
    else:
        main()
