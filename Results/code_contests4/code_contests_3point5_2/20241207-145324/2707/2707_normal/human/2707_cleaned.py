(n, n1, n2) = (int(i) for i in raw_input().split())
a = [int(i) for i in raw_input().split()]
a.sort()
if n1 > n2:
    (n1, n2) = (n2, n1)
s1 = 0
for i in range(n1):
    s1 += a[n - i - 1]
s2 = 0
for i in range(n2):
    s2 += a[n - n1 - i - 1]
print(1.0 * s1 / n1 + 1.0 * s2 / n2)