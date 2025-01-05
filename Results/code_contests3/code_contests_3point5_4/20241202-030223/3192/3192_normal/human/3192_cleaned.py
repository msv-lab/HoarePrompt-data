n = int(raw_input())
arr = []
maxval = 0
arr2 = []
for i in xrange(n):
    arr1 = list(map(int, raw_input().split()))
    temp = 0
    for j in xrange(1, arr1[0]):
        temp = max(temp, arr1[j])
    arr.append(temp)
    arr2.append(arr1[0])
    maxval = max(arr[i], maxval)
ans = 0
for i in range(n):
    ans += (maxval - arr[i]) * arr2[i]
print(ans)