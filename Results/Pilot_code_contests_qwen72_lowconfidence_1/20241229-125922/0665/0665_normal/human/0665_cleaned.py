buffer = io.BytesIO()
sys.stdout = buffer

@atexit.register
def func_1():
    sys.__stdout__.write(buffer.getvalue())
n = int(raw_input())
l = [int(x) for x in raw_input().split()]
l.sort()
mx = l[n - 1]
x = math.log(mx, 2)
c = pow(2, x / (n - 1))
floor_c = int(c)
if floor_c <= 0:
    floor_c += 1
nxt_num = floor_c + 1
ans = pow(10, 16)
res = 0
mul = 1
c = floor_c
for i in range(0, n):
    res += abs(mul - l[i])
    mul = mul * c
ans = min(ans, res)
res2 = 0
mul = 1
c = nxt_num
for i in range(0, n):
    res2 += abs(mul - l[i])
    mul = mul * c
ans = min(ans, res2)
print(int(ans))