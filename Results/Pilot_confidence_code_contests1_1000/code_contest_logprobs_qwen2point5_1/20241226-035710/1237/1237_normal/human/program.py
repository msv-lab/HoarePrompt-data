import collections
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
t = rri()

def solve(n, k, arr):
    dic = collections.Counter()
    for x in arr:
        if x%k:
            dic[x%k]+=1
    if not len(dic):
        return 0
    def get(key, value):
        return k-key + (value-1)*k
    ans = 0
    for key, value in dic.items():
        ans = max(ans, get(key, value))
    return ans+1
    
for _ in range(t):
    n, k = rrm()
    arr = rrm()
    print(solve(n, k, arr))
    