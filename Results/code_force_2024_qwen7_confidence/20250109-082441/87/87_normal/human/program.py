from collections import Counter
t = int(input())
for _ in range(t):
    n,x,y = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    hashmap = Counter(arr)
    count = 0
    for x in arr:
        if not hashmap[x-1] and hashmap[x-2]:
            count+=1
    if hashmap[1] and hashmap[n-1] and not hashmap[n]:
        count+=1
    if hashmap[2] and hashmap[n] and not hashmap[1]:
        count+=1
    
    print(count+len(arr)-2)