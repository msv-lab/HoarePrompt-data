(n, k) = map(int, input().split())
l = (n + k - 1) // (k * 2 + 1)
res = []
for i in range(l):
    res.append(i * (k * 2 + 1) + 1)
print(l)
print(' '.join(map(str, res)))