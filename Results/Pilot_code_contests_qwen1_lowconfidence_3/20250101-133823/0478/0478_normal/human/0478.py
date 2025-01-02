# <editor-fold desc="Fast IO">
# !/usr/bin/env python
from __future__ import division, print_function

import itertools
import os
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

BUFFER_SIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFFER_SIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFFER_SIZE))
            self.newlines = b.count(b'\n') + (not b)
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
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
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
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip('\r\n')

# </editor-fold>

import collections


def solve(num):
    num = [ord(x) - ord('0') for x in num]

    even_digits, odd_digits = collections.deque(), collections.deque()

    for digit in num:
        if digit & 1 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)

    ret = []

    for _ in range(len(num)):
        if not odd_digits or (even_digits and even_digits[0] < odd_digits[0]):
            ret.append(even_digits.popleft())
        else:
            ret.append(odd_digits.popleft())

    return ''.join(map(str, ret))


# xx


DEBUG = False

if not DEBUG:
    t = int(input())

    while t > 0:
        t -= 1
        s = input()
        print(solve(s))

else:
    print(solve('246432'))
    print(solve('2464321'))
    print(solve('264721'))
    #
    print(solve('999999992222222'))
    print(solve('7772648'))
    print(solve('737572464282'))

    print(solve('12'))
    print(solve('21'))
    print(solve('221'))
    print(solve('221'))
