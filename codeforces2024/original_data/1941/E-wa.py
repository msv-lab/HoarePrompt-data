from collections import deque
t = int(input())
for _ in range(t):
    n,m,k,d = map(int,input().split())

    ans = []
    for _ in range(n): # d - 1 
        row = list(map(int,input().split()))
        row = list(map(lambda x : x + 1,row))
        cache = [0] * m
      
        queue = deque([0])
        cache[0] = row[0]
        for i in range(1,m): #0 3 3 0
            cache[i] += cache[queue[0]] + row[i]
            
            while queue and cache[queue[-1]] > cache[i]:
                queue.pop()

            queue.append(i) 
            if (i - queue[0]) > d:
                queue.popleft()
            
        ans.append(cache[-1])

    #pick k of them
    left = 0
    runningSum = 0
    res = sum(ans)
    for right in range(len(ans)):
        runningSum += ans[right]
        if right >= k:
            runningSum -= ans[left]
            left += 1

            res = min(res,runningSum)        

    print(res)

    