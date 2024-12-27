n,k = map(int,raw_input().split())
arr = list(map(int,raw_input().split()))
freq = dict()
for i in arr:
    freq[i] = freq.get(i,0)
    freq[i] += 1
arr = list(set(arr))
arr.sort(reverse=True)
ans = freq[arr[0]]
pres = arr[0]
for i in arr[1:]:
    if pres > i and pres <= i+k :
        pass
    else:
        ans += freq[i]
    pres = i
print(ans)
