import os
import sys
from atexit import register
from io import BytesIO

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')

# ref. https://codeforces.com/blog/entry/71884
# 1) inp(), For taking integer inputs.
# 2) inlt(), For taking List inputs.
# 3) insr(), For taking string inputs. 
#           Actually it returns a List of Characters, 
#           instead of a string, which is easier to use in Python, 
#           because in Python, Strings are Immutable.
# 4) invr(), For taking space seperated integer variable inputs.

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

def gcd(a, b):
    while a % b > 0:
        c = a % b
        a = b
        b = c
    
    return b

def findC(l, r):
    for a in range(l, r + 1):
        for b in range(a + 1, r + 1):
            # print(a, b, r, gcd(b, a), gcd(r, b))
            if gcd(r, b) == 1 and gcd(b, a) != 1:
                return (a, b, r)

    return (-1, -1, -1)

l, r = inlt()

if gcd(r, l) == 1:
    a, b, c = findC(l, r)
    if a == -1:
        sys.stdout.write('-1\n')
    sys.stdout.write(str(a) + ' ' + str(b)+ ' ' + str(c) + '\n')
else:
    sys.stdout.write(str(l) + ' ' + str(l + 1)+ ' ' + str(r) + '\n')
