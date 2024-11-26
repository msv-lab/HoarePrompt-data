n = int(raw_input())
arr = list(map(int,raw_input().split()))
freq = dict()
vis = dict()
for i in arr:
    freq[i] = freq.get(i,0)
    if not freq[i]:
        vis[i] = 0 
    freq[i] += 1
rem = len(set(arr))
ans = 0
for i in arr:
    freq[i] -=1
    if not freq[i]:
        rem-=1
    if not vis[i]:
        ans += rem
        vis[i] = 1
print(ans)
