n = int(input())
a = []
g = []
for _ in range(n):
    a_i, g_i = map(int, input().split())
    a.append(a_i)
    g.append(g_i)

# Distribute the eggs
result = ''
for i in range(n):
    if abs(sum(a) + g[i] - sum(g) - a[i]) <= 500:
        result += 'A'
        a[i] = 1000 - g[i]
    else:
        result += 'G'
        g[i] = 1000 - a[i]

# Check if distribution is possible
if abs(sum(a) - sum(g)) <= 500:
    print(result)
else:
    print(-1)