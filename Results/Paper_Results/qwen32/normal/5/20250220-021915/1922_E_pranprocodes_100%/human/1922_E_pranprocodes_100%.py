for i in range(int(input())):
    x=int(input())
    max=100000000
    min=-100000000
    ans=[]
    t=0
    while x!=1:
        if x%2==0:
            ans.append(max)
            max-=1
            x=x//2
        else:
            ans.append(min)
            min+=1
            x-=1
        t+=1
    ans.reverse()    
    print(t)
    print(*ans)