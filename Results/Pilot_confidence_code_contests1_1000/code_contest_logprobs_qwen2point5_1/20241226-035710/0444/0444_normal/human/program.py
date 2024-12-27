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
                  
def solve(arr, n, x, m):
    ans = 1
    before = [x,x]
    for a, b in arr:
        if a<=before[0] and before[0]<=b<=before[1]:
            ans+=before[0] -a
            before = [a, before[1]]
        elif before[0]<=a<=before[1] and b>=before[1]:
            ans += b-before[1]
            before = [before[0], b]
        elif a<=before[0] and b>=before[1]:
            ans += before[0]-a
            ans+= b-before[1]
            before = [a, b]
    return ans
t  = rri()
for _ in range(t):
    n, x, m = rrm()
    arr = []
    for _ in range(m):
        arr.append(rrm())
    print(solve(arr, n, x, m))
    