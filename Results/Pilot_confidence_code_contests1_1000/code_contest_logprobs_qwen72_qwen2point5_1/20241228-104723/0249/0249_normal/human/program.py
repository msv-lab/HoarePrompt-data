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
rrmm = lambda n: [rrm() for _ in xrange(n)]
N = rri()
arr = rrm()
def solve(N, arr):
    memo = {}
    def find(status, cur_money, idx):
        if (status, cur_money, idx) in memo:
            return memo[(status, cur_money, idx)]
        if idx == N-1:
            if not status:
                return cur_money
            else:
                return cur_money+ status * arr[idx]
        ans = cur_money
        if status == 0:
            nxt_status = cur_money//arr[idx]
            nxt_money = cur_money % arr[idx]
            for i in range(idx+1, N):
                ans = max(find(nxt_status, nxt_money, i), ans)
                ans = max(ans, find(status, cur_money, i))
        else:
            nxt_status = 0
            nxt_money = cur_money+status*arr[idx]
            for i in range(idx+1, N):
                ans = max(find(nxt_status, nxt_money, i), ans)
                ans = max(ans, find(status, cur_money, i))
        memo[(status, cur_money, idx)] = ans;
        return ans
    return find(0, 1000, 0)
print(solve(N, arr))
        