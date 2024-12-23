(n, k) = map(str, input().split())
k = int(k)
count_zeros = 0
to_remove = 0
for digit in reversed(n):
    if digit == '0':
        count_zeros += 1
    else:
        to_remove += 1
    if count_zeros == k:
        break
if count_zeros == k:
    print(to_remove)
else:
    print(len(n) - 1)