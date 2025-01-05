FAST_IO = 1
if FAST_IO:
    import io, sys, atexit
    rr = iter(sys.stdin.read().splitlines()).next
    sys.stdout = _OUTPUT_BUFFER = io.BytesIO()

    @atexit.register
    def write():
        sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
else:
    rr = raw_input
rri = lambda : int(rr())
rrm = lambda : map(int, rr().split())

def func_1(A, B, V, W, T):
    la = A + V * T
    lb = B + W * T
    if A < B:
        return la >= lb
    else:
        return lb >= la
(A, V) = rrm()
(B, W) = rrm()
T = rri()
ans = func_1(A, B, V, W, T)
if ans:
    print('YES')
else:
    print('NO')