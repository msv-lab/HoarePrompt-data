from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]

def solve(N):
    P = nl()

    a = [10**5]
    b = [10**5]
    fail = False
    for c in P[::-1]:
        if len(a) == 1:
            a.append(c)
            continue
        if c > a[-1] and c > b[-1]:
            fail = True
            break
        if c > a[-1]:
            a.append(c)
            continue
        if c > b[-1]:
            b.append(c)
            continue
        if (len(b), b[-1]) < (len(a), a[-1]):
            b.append(c)
        else:
            a.append(c)
    if len(a) != N +1: fail = True
    if fail:
        print('NO')
    else:
        print('YES')

t = ni()
for _ in range(t):
    N = ni()
    solve(N)
