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



def solve(n, m,arr, topic):
    for a, b in arr:
        if topic[a-1] == topic[b-1]:
            return -1
    return ' '.join([str(i) for i in range(1, n+1)])

n, m = rrm()
graph = []
for _ in range(m):
    graph.append(rrm())
topic = rrm()
print(solve(n, m, graph, topic))
