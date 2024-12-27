from heapq import heappush, heappop

n = int(raw_input())
p = map(int, raw_input().split())

h, ans = [], 0
for i in range(n):
    if len(h) > 0 and p[i] > h[0]:
        ans += p[i] - h[0]
        heappop(h)
        heappush(h, p[i])
    heappush(h, p[i])
print (ans)
