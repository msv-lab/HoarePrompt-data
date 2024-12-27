# PYTHON3---------------------------------------------------------------------#
from __future__ import division, print_function
range = xrange

# IMPORTS---------------------------------------------------------------------#
import math
import operator
import random
from atexit import register
from collections import Counter, defaultdict, deque
from fractions import Fraction, gcd
from io import BytesIO
#from decimal import Decimal, getcontext
from itertools import combinations, permutations, product
from Queue import PriorityQueue, Queue
from string import ascii_lowercase, ascii_uppercase
from sys import __stdout__, setrecursionlimit, stdin, stdout

# SETTINGS--------------------------------------------------------------------#
#getcontext().prec = 100
#setrecursionlimit(100000)

# CONSTANTS-------------------------------------------------------------------#
MOD = 10**9 + 7
INF = float('+inf')

# FASTIO----------------------------------------------------------------------#
stdout = BytesIO()
register(lambda: __stdout__.write(stdout.getvalue()))
#stdin = BytesIO(stdin.read())

input = lambda: stdin.readline().rstrip()
print = lambda *args: stdout.write(' '.join(str(x) for x in args) + '\n')
flush = stdout.flush()

# MAIN------------------------------------------------------------------------#
def main():
    q = int(input())
    for _ in range(q):
        n, m, k = map (int, input().split())
        
        if k < max(n, m):
            print(-1)
        else:
            if n == m:
                if (k - n) % 2 == 0:
                    print(k)
                else:
                    print(k-2)
            else:
                if (m-n) % 2 == 0:
                    steps = max(n, m)
                    if (k - steps) % 2 == 0:
                        print(k)
                    else:
                        print(k-2)
                else:
                    steps = max(m, n)
                    if (k - steps) % 2 == 0:
                        print(k-1)
                    else:
                        print(k-1)                    
                    


if __name__ == '__main__':
    main()