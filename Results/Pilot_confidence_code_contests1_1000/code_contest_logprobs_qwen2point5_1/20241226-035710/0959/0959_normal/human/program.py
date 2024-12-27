import sys
n = int(raw_input())
color = []
for i in xrange(n):
    color.append(map(int,raw_input().split()))
m = {}
left = {}
for u,v in color:
    if m.has_key(u): m[u] += 1
    else: m[u] = 1
    if left.has_key(u): left[u] += 1
    else: left[u] = 1
    if u == v: continue
    if m.has_key(v):
        m[v] += 1
    else:
        m[v] = 1
ans = n+1
for u,v in color:
    if left[u] * 2 >= n:
        ans = 0
        break
    if m[u] * 2 >= n:
        ans = min(ans, (n+1)/2 - left[u])
print -1 if ans == n+1 else ans
