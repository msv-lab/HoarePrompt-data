(n, k) = map(int, raw_input().split())
ls = map(int, raw_input().split())
tmp = ls[k - 1]
check = True
for i in range(k, n):
    if ls[i] != tmp:
        check = False
if check:
    print(k - 1)
else:
    print(-1)