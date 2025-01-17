import heapq
rs=[]
for _ in range(int(input())):
    n,m = map(int,input().split())
    l=list(map(int,input().split()))
    mx=0;s=0
    cnt=0
    h=[]
    for i in range(n):
        if s>=l[i]:
            s-=l[i]
            heapq.heappush(h,-l[i])
            cnt+=1
            mx=max(mx,cnt)
        else:
            if h:
                if l[i]<abs(h[0]):
                    s+=abs(h[0])-l[i]
                    heapq.heappop(h)
                    heapq.heappush(h,-l[i])
        s+=m                    


    rs.append(cnt)
print(*rs,sep="\n")        



        

