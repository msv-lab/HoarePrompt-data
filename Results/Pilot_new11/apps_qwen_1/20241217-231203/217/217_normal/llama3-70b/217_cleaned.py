n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
(b, c) = (0, 0)
for i in range(n):
    if i % 2 == 0:
        b += a[i]
    else:
        c += a[i]
print(b - c)