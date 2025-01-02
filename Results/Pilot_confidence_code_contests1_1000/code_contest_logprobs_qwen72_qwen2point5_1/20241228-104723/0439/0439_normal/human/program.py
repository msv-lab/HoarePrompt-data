s=''
for i in range(1,28342):
    s+=str(i)
def getNthChar(n):
    return s[n]
P=28342
dp=[0]*(P)
for i in range(1,10):
    dp[i]=i
for i in range(10,100):
    dp[i]=(i-9)*2+9
prev=dp[99]
for i in range(100,1000):
    dp[i]=(i-99)*3+dp[99]
for i in range(1000,10000):
    dp[i]=(i-999)*4+dp[999]
for i in range(10000,P):
    dp[i]=(i-9999)*5+dp[i-9999]
for i in range(1,P):
    dp[i]+=dp[i-1]
#print(dp[10**4])
for _ in range(int(raw_input())):
    k=int(raw_input())
    lo=0
    hi=P-1
    while lo<=hi:
        mi=(lo+hi)>>1
        if dp[mi]==k:
            ans=mi
            break
        if dp[mi]<=k:
            ans=mi
            #print(ans)
            lo=mi+1
        else:
            hi=mi-1
    mi=ans
    rem=k-dp[mi]
    #print(rem)
    print(getNthChar(rem-1))