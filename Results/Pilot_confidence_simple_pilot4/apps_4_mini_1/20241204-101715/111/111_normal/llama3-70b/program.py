n = int(input())
a = list(map(int, input().split()))

cnt_neg = 0
cnt_zero = 0
for i in range(n):
    if a[i] < 0:
        cnt_neg += 1
    elif a[i] == 0:
        cnt_zero += 1

if cnt_neg % 2 == 1:
    for i in range(n):
        if a[i] > 0:
            a[i] = -a[i] - 1
else:
    for i in range(n):
        if a[i] < 0:
            a[i] = -a[i] - 1

for i in range(n):
    print(a[i], end=' ')
print()
