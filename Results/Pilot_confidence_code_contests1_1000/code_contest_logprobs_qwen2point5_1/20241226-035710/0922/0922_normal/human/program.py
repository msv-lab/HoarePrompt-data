a, b, c, d, n = map(int, raw_input().split())
res = ["." * (a+c)] * max(b, d)
for i in range(b):
    for j in range(a):
        res[i] = res[i][:j]+"?"+res[i][j+1:]
for i in range(d):
    for j in range(c):
        res[i] = res[i][:a+j]+"?"+res[i][a+j+1:]

i = 0
if b > d:
    j = 0 if d%2 == 0 else a+c-1
else:
    j = a+c-1 if b%2 == 0 else 0

k = 0
for size in map(int, raw_input().split()):
    for _ in range(size):
        assert res[i][j] == '?'
        res[i] = res[i][:j]+chr(ord('a')+k)+res[i][j+1:]
        if j-1 >= 0 and res[i][j-1] == '?':
            j -= 1
        elif j+1 < len(res[i]) and res[i][j+1] == '?':
            j += 1
        else:
            i += 1
    k += 1

for s in res:
    print(s)
