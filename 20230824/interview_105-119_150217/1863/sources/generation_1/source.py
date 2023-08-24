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
    if abs(sum(a[:i+1]) - sum(g[:i+1])) <= 500:
        result += 'A'
        a[i], g[i] = 0, 1000
    else:
        result += 'G'
        a[i], g[i] = 1000, 0

# Check if distribution is possible
if abs(sum(a) - sum(g)) <= 500:
    print(result)
else:
    print(-1)