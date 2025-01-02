n = int(raw_input())
a = [int(x) for x in raw_input().split()]
'\nmax_avg = 0\nmax_len = 0\nfor i in range(0, n):\n    for j in range(i, n):\n        tmp = sum(a[i:j+1])/float(j-i+1)\n        if tmp > max_avg:\n            max_avg = tmp\n            max_len = (j-i+1)\n        elif tmp == max_avg:\n            if (j-i+1) > max_len:\n                max_len = (j-i+1)\n'
max_a = max(a)
max_len = 0
tmp = 0
for i in range(0, n):
    if a[i] != max_a:
        if tmp > max_len:
            max_len = tmp
        tmp = 0
    elif a[i] == max_a:
        tmp += 1
if tmp > max_len:
    max_len = tmp
print(max_len)