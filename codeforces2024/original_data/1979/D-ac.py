for _ in range(int(input())):
    n,k,=map(int,input().split())
    s=input()
    temp=[s[0]*k,str(1-int(s[0]))*k]
    x="".join([temp[i%2]for i in range(n//k)])
    y="".join([temp[1-i%2]for i in range(n//k)])
    ans=n
    for i in range(n):
        if s[i]!=x[i]:
            j=i
            while(j<n and s[j]==s[i]): j+=1
            s=s[j-k:]+s[:j-k][::-1]
            ans=(j-k if j-k>0 else k-(j-k)%k)
            if s!=y and s!=x:
                 ans=-1
            break
    print(ans)
