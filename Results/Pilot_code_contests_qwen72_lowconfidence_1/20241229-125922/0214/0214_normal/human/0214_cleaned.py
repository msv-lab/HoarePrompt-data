"""
This file is part of https://github.com/Cheran-Senthil/PyRival.

Copyright 2018 Cheran Senthilkumar all rights reserved,
Cheran Senthilkumar <hello@cheran.io>
Permission to use, modify, and distribute this software is given under the
terms of the MIT License.

"""
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream
    from math import gcd
if sys.version_info[0] < 3:

    class dict(dict):
        """dict() -> new empty dictionary"""

        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)

        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)

        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)

    def gcd(x, y):
        """gcd(x, y) -> int
        greatest common divisor of x and y
        """
        while y:
            (x, y) = (y, x % y)
        return x
    input = raw_input
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def func_1(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.

    Args:
        sync (bool, optional): The new synchronization setting.

    """
    global input, flush
    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda : sys.stdin.readline().rstrip('\r\n')
        sys.stdout = stream()
        register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))

def func_2():
    t = int(input())
    for i in range(t):
        (n, m) = map(int, input().split(' '))
        white_sq_0 = (n * m + 1) // 2
        (x1, y1, x2, y2) = map(int, input().split(' '))
        col_cnt_1 = x2 - x1 + 1
        row_cnt_1 = y2 - y1 + 1
        if x1 % 2 == 0:
            if y1 % 2 == 0:
                white_sq_1 = (col_cnt_1 * row_cnt_1 + 1) // 2
            else:
                white_sq_1 = col_cnt_1 * row_cnt_1 // 2
        elif y1 % 2 == 0:
            white_sq_1 = col_cnt_1 * row_cnt_1 // 2
        else:
            white_sq_1 = (col_cnt_1 * row_cnt_1 + 1) // 2
        (x3, y3, x4, y4) = map(int, input().split(' '))
        col_cnt_2 = x4 - x3 + 1
        row_cnt_2 = y4 - y3 + 1
        if x3 % 2 == 0:
            if y3 % 2 == 0:
                white_sq_2 = (col_cnt_2 * row_cnt_2 + 1) // 2
            else:
                white_sq_2 = col_cnt_2 * row_cnt_2 // 2
        elif y3 % 2 == 0:
            white_sq_2 = col_cnt_2 * row_cnt_2 // 2
        else:
            white_sq_2 = (col_cnt_2 * row_cnt_2 + 1) // 2
        if x3 > x2 or y3 > y2 or x4 < x1 or (y4 < y1):
            white_cnt = white_sq_0 + (col_cnt_1 * row_cnt_1 - white_sq_1) - white_sq_2
            black_cnt = n * m - white_cnt
            print(white_cnt, black_cnt)
        else:
            (x5, x6) = (max(x1, x3), min(x2, x4))
            (y5, y6) = (max(y1, y3), min(y2, y4))
            col_cnt_3 = x6 - x5 + 1
            row_cnt_3 = y6 - y5 + 1
            if x5 % 2 == 0:
                if y5 % 2 == 0:
                    white_sq_3 = col_cnt_3 * row_cnt_3 // 2
                else:
                    white_sq_3 = (col_cnt_3 * row_cnt_3 + 1) // 2
            elif y5 % 2 == 0:
                white_sq_3 = (col_cnt_3 * row_cnt_3 + 1) // 2
            else:
                white_sq_3 = col_cnt_3 * row_cnt_3 // 2
            white_cnt = white_sq_0 + (col_cnt_1 * row_cnt_1 - white_sq_1) - white_sq_2
            black_cnt = n * m - white_cnt
            print(white_cnt - white_sq_3, black_cnt + white_sq_3)
if __name__ == '__main__':
    func_1(False)
    func_2()