"""input
4
6 4 2
2 9 2 3 8 5
4 4 1
2 13 60 4
4 1 3
1 2 2 1
2 2 0
1 2
"""
debug = 1
readln = sys.stdin.readline
sys.setrecursionlimit(4000)

def func_1(s):
    sys.stdout.write(str(s))

def func_2(s):
    sys.stdout.write(str(s))
    sys.stdout.write('\n')

def func_3():
    return int(readln().strip())

def func_4():
    return map(int, readln().split())

def func_5():
    return readln().strip()

def func_6():
    return readln().split()

def func_7(*args):
    if debug:
        print(' '.join(map(str, args)))

def func_8(l, r, k, A, prilist, pri_idx, seglen):
    for pi in xrange(pri_idx, len(prilist) - 1):
        (v, pl, pr) = prilist[pi]
        lcut = max(0, pl - l + 1)
        rcut = max(0, r - pr + 1)
        if lcut == 0 or rcut == 0:
            continue
        ans = 0
        if lcut <= k and r - pl >= seglen:
            ans = max(ans, func_8(pl + 1, r, k - lcut, A, prilist, pi + 1, seglen))
        if rcut <= k and pr - l >= seglen:
            ans = max(ans, func_8(l, pr - 1, k - rcut, A, prilist, pi + 1, seglen))
        if ans:
            return ans
        else:
            break
    ans = 10000000000.0
    for i in xrange(l, r + 1):
        if i + seglen - 1 > r:
            break
        ans = min(ans, max(A[i], A[i + seglen - 1]))
    return ans
t = func_3()
for _ in xrange(t):
    (n, m, k) = func_4()
    A = func_4()
    seglen = n - m + 1
    prilist = sorted([(max(A[i], A[i + seglen - 1]), i, i + seglen - 1) for i in xrange(0, len(A)) if i + seglen - 1 < len(A)])
    func_2(func_8(0, len(A) - 1, k, A, prilist, 0, seglen))