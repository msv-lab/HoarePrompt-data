from sys import stdin 
n, m = map(int, stdin.readline().split())
ans = []
mm = -m
while n:
    ff = n/mm
    if ff * mm > n:
        ff = ff + 1
    ans.append(n - ff * mm)
    n = ff

l = len(ans)
print(l)
for i in range(0, l):
    res = ans[i]
    if res < 0:
        res += m
    print(res),