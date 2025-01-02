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

T = ni()
def swap(ch):
    return '1' if ch == '0' else '0'

def get_a_l(a, flips):
    if flips%2 == 0:
        return a[0]
    else:
        return swap(a[-1])

def get_a_r(a, flips):
    if flips%2 == 0:
        return a[-1]
    else:
        return swap(a[0])

def solve(a, b):
    a = deque(a)
    out = []
    flips = 0
    for i in range(len(a) - 1, -1, -1):
        if (get_a_r(a, flips) == b[i]):
            if flips%2 == 0:
                a.pop()
            else:
                a.popleft()
            continue
        if (get_a_l(a, flips) != b[i]):
            out.append(i+1)
        else:
            out.append(1)
            out.append(i+1)
        flips += 1
        if flips%2 == 0:
            a.pop()
        else:
            a.popleft()
    return out

for _ in range(T):
    N = ni()
    a = list(inp())
    b = list(inp())
    out = solve(a, b)
    print(' '.join(map(str, [len(out)] + out)))
    
    
