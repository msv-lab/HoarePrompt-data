#!/usr/bin/env python
from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import random
import collections
import math
import itertools

def real_main():
    N = read_int()
    balls = []
    for _ in range(N):
        balls.append(read_int_array())
    print(solve(N, balls))


def solve(n, balls):
    bdict = collections.defaultdict(set)
    for x, y in balls:
        bdict[x].add(y)

    def score(p, q):
        out = n
        for x, y in balls:
            nx, ny = x + p, y + q
            if ny in bdict.get(nx, []):
                out -= 1
        return out

    tried = set()
    ans = n
    for i in range(n):
        for j in range(i):
            p, q = balls[j][0] - balls[i][0], balls[j][1] - balls[i][1]
            if (p, q) not in tried:
                tried.add((p, q))
                tried.add((-p, -q))

                points = score(p, q)
                if points < ans:
                    ans = points
    return ans



def main():
    if False and 'PYCHARM_HOSTED' in os.environ:
        main_pycharm()
    else:
        real_main()


from copy import deepcopy
def main_pycharm():
    solution = solve

    test_inputs = None
    test_outputs = None
    judge = None
    slow_solution = None
    if solution is not None:
        if test_outputs is not None:
            test_with_answers(solution, test_inputs, test_outputs)
        if judge is not None:
            test_with_judge(solution, test_inputs, judge)
        if slow_solution is not None:
            test_with_slow_solution(solution, test_inputs, slow_solution)


def test_with_answers(solution, inputs_answers):
    total, wrong = 0, 0
    for args, test_ans in inputs_answers:
        ans = solution(*args.copy())
        if ans != test_ans:
            print('WRONG! ans=%s, test_ans=%s, args=%s' % (ans, test_ans, args))
            wrong += 1
        else:
            print('GOOD')
        total += 1
    print('ALL %d TESTS PASSED' % total if not wrong else '%d out of %d tests are WRONG' % (wrong, total))


def test_with_judge(solution, inputs_gen, judge):
    total, wrong = 0, 0
    for args in inputs_gen:
        ans = solution(*deepcopy(args))
        if not judge(deepcopy(ans), *deepcopy(args)):
            print('WRONG! ans=%s, args=%s' % (ans, args))
            wrong += 1
        total += 1
    print('ALL %d TESTS PASSED' % total if not wrong else '%d out of %d tests are WRONG' % (wrong, total))


def test_with_slow_solution(solution, inputs_gen, solution_slow):
    total, wrong = 0, 0
    for args in inputs_gen:
        ans = solution(*deepcopy(args))
        slow = solution_slow(*deepcopy(args))
        if ans != slow:
            print('WRONG! ans=%s, slow=%s, args=%s' % (ans, slow, args))
            wrong += 1
        total += 1
    print('ALL %d TESTS PASSED' % total if not wrong else '%d out of %d tests are WRONG' % (wrong, total))


# region fastio

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
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")

read = input
read_int = lambda: int(input())
read_array = lambda sep=None, maxsplit=-1: input().split(sep, maxsplit)
read_int_array = lambda: [int(a) for a in read_array()]

# endregion

if __name__ == "__main__":
    main()
