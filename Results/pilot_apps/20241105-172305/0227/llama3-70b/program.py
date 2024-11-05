n = int(input())
a = list(map(int, input().split()))
a.sort()
m = 1
for i in range(1, n):
    if a[i] != a[i-1] * 2:
        m += 1
print(m if m <= 23 else -1)
