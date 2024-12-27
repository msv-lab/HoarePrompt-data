from __future__ import division, print_function

import sys
from atexit import register

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream


sys.stdin = stream(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')

sys.stdout = stream()
register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


def read_int():
    return int(input())


def read_ints():
    return list(map(int, input().split(' ')))


def solve():
    n, m = read_ints()
    table = []
    for _ in range(n):
        table.append(input())

    def create_table():
        return [[1 for _ in range(m)] for _ in range(n)]

    top_left = create_table()
    top_right = create_table()
    bottom_left = create_table()
    bottom_right = create_table()

    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0 and table[i-1][j] == table[i][j-1] == table[i][j]:
                top_left[i][j] = min(top_left[i-1][j], top_left[i][j-1])+1

    for i in range(n):
        for j in range(m-1, -1, -1):
            if i > 0 and j < m-1 and table[i-1][j] == table[i][j+1] == table[i][j]:
                top_right[i][j] = min(top_right[i-1][j], top_right[i][j+1])+1

    for i in range(n-1, -1, -1):
        for j in range(m):
            if i < n-1 and j > 0 and table[i+1][j] == table[i][j-1] == table[i][j]:
                bottom_left[i][j] = min(bottom_left[i+1][j], bottom_left[i][j-1])+1

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i < n-1 and j < m-1 and table[i+1][j] == table[i][j+1] == table[i][j]:
                bottom_right[i][j] = min(bottom_right[i+1][j], bottom_right[i][j+1])+1

    answer = 0
    for i in range(n):
        for j in range(m):
            answer += min(top_left[i][j], top_right[i][j], bottom_left[i][j], bottom_right[i][j])
    return answer

if __name__ == '__main__':
    print(solve())
