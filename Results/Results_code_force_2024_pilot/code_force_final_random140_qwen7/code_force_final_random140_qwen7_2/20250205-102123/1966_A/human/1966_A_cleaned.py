t = int(input())
while t > 0:
    (n, k) = map(int, input().split())
    arrC = list(map(int, input().split()))
    hashmap = {}
    ans = n
    for i in arrC:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
        if hashmap[i] >= k:
            ans = k - 1
    print(ans)
    t -= 1