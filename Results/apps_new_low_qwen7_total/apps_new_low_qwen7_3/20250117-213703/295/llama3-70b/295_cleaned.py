n = int(input())
a = list(map(int, input().split()))
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
f = False
for i in range(12):
    if all((a[j] == b[(i + j) % 12] for j in range(n))):
        f = True
    if i == 11 and (not f):
        break
    if all((a[j] == b[(i + j) % 12 + 12] for j in range(n))):
        f = True
    if i == 11 and (not f):
        break
if f:
    print('YES')
else:
    print('NO')