for _ in range (int(input())): 
    n , m = map(int,input().split()) 
    aseg = [0]*(n+2) 
    along = [-1]*(n+2) 
    for i in range (m): 
        l , r = map(int, input().split()) 
        aseg[l] += 1 
        aseg[r+1] -=1 
        along[l] = max(r+1, along[l])
    dp = [0]*(n+2) 
    for i in range (n): 
        aseg[i+1] += aseg[i] 
        along[i] = max(along[i] , along[i-1])
    for i in range (n, 0 , -1): 
        if along[i] < 0 : dp[i] = dp[i+1] 
        else:dp[i] = max(dp[i+1] , aseg[i] + dp[along[i]])
    # print(dp) 
    # print(aseg) 
    # print(along)
    print(dp[1])
    
    