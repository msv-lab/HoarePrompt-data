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


dic = {}
def f(x):
    if x in dic:
        return dic[x]
    if x== 0:
        return 0
    tmp = x% bin(x).count('1')
    dic[x] = f(tmp)+1
    return dic[x]
    
N = rri()
num = int('0b'+rr(),2)
count = bin(num).count('1')
for i in range(N):
    if not num & (1<<(N-i-1)):
        cur_count = count+1
    else:
        cur_count =count-1
    if cur_count ==0:
        print(0)
    else:
        cur_num = num ^ (1<<(N-i-1))
        cur_num = cur_num%cur_count
        print(f(cur_num)+1)
