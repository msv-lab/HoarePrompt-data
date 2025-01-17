n = int(input())
a = list(map(int, input().split()))
d = [0] * n
left = float('inf')
for i in range(n):
    if a[i] == 0:
        left = 0
    else:
        left += 1
    d[i] = left
right = float('inf')
for i in range(n-1, -1, -1):
    if a[i] == 0:
        right = 0
    else:
        right += 1
    d[i] = min(d[i], right)
print(' '.join(map(str, d)))
