(a, b) = raw_input().split()
n = int(a)
i = int(b)
i = i - 1
p = range(1, n + 1)
for k in range(1, n + 1):
    f = factorial(n - k)
    d = i // f
    (print(p[d]),)
    p.remove(p[d])
    i = i % f