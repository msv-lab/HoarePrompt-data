from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
n, m = rints()
a, b = rints(), [rints() for _ in range(m)]
adj, tem, ans = [set() for _ in range(n + 1)], [], 0
adj2 = set()

for u, v in b:
    adj[u].add(v)
    if v == a[-1]:
        adj2.add(u)

for i in range(n - 2, -1, -1):
    if a[i] in adj2:
        if len(adj[a[i]]) >= len(tem):
            ans += 1
            for j in tem:
                if j not in adj[a[i]]:
                    ans -= 1
                    break
    else:
        tem.append(a[i])

print(ans)
