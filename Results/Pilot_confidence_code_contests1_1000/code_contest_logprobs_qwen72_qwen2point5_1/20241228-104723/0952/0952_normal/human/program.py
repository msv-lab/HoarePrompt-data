import math as mt 
from collections import Counter, defaultdict
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
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split())


def solve(N, arr):
    num_even, num_odd = 0, 0
    even, odd = [], []
    for i in range(N*2):
        if arr[i]%2:
            num_odd+=1
            odd.append(i)
        else:
            num_even+=1
            even.append(i)
    if len(even)>=2*(N-1):
        return even[:2*N-2]
    else:
        N-=1
        N-= len(even)/2
        return even[:(len(even)-len(even)%2)]+odd[:2*N]
t = rri()
for _ in range(t):
    n = rri()
    arr = rrm()
    ans = solve(n, arr)
    for i in range(n-1):
        print(str(ans[2*i]+1)+' '+str(ans[2*i+1]+1))
    