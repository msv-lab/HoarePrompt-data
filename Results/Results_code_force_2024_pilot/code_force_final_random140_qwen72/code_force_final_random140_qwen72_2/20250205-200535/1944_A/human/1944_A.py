def fun(n, k):
    
    
    if k>=n-1:
        return 1
    else:
        return n
    
 
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(fun(n, k))