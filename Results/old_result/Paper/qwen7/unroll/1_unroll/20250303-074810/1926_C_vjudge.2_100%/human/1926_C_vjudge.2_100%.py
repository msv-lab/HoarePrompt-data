N = int(2 * 10e4) + 1
 
t = int(input())
 
pd = [0 for _ in range(N)]
 
for i in range(1, N):
    pd[i] += pd[i - 1]    
    for j in str(i):
        pd[i] += int(j)
 
for _ in range(t):    
    n = int(input())
    print(pd[n])