if __name__=="__main__":
    t=int(input())
    while t:
        n=int(input())
        a=list(map(int,input().split()))
        a=sorted(a[i]+i+1 for i in range(n))[::-1]
        for i in range(1,n):
            a[i]=min(a[i],a[i-1]-1)
        print(*a)    
        t-=1    
        
  