n = int(raw_input())
a = list(map(int, raw_input().split()))
k = 0
for i in range(n - 1):
    if a[i] > a[i + 1]:
        k += 1
if k <= 2:
    print('YES')
else:
    print('NO')