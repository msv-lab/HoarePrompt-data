'''input
4
6 4 2
2 9 2 3 8 5
4 4 1
2 13 60 4
4 1 3
1 2 2 1
2 2 0
1 2
'''

import sys
debug = 1
readln = sys.stdin.readline
sys.setrecursionlimit(4000)

def write(s):
    sys.stdout.write(str(s))

def writeln(s):
    sys.stdout.write(str(s))
    sys.stdout.write('\n')

def readint():
    return int(readln().strip())

def readints():
    return map(int, readln().split())

def readstr():
    return readln().strip()

def readstrs():
    return readln().split()

def dprint(*args):
    if debug: print(' '.join(map(str, args)))

def solve(l, r, k, A, prilist, pri_idx, seglen):
    for pi in xrange(pri_idx, len(prilist) - 1):
        v, pl, pr = prilist[pi]
        lcut = max(0, pl - l + 1)
        rcut = max(0, r - pr + 1)
        if lcut == 0 or rcut == 0: continue

        ans = 0
        if lcut <= k and (r-pl) >= seglen:
            ans = max(ans, solve(pl+1, r, k-lcut, A, prilist, pi+1, seglen))

        if rcut <= k and (pr-l) >= seglen:
            ans = max(ans, solve(l, pr-1, k-rcut, A, prilist, pi+1, seglen))

        if ans:
            return ans
        else:
            break

    # calc ans
    ans = 10e9
    for i in xrange(l, r+1):
        if i+seglen-1 > r: break
        ans = min(ans, max(A[i], A[i+seglen-1]))
    return ans

t = readint()
for _ in xrange(t):
    n,m,k = readints()
    A = readints()
    seglen = n-m+1
    prilist = sorted([(max(A[i], A[i+seglen-1]), i, i+seglen-1) for i in xrange(0, len(A)) if i+seglen-1 < len(A)])
    writeln(solve(0, len(A)-1, k, A, prilist, 0, seglen))