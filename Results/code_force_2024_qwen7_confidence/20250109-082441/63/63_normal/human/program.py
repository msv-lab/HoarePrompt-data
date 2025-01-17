from audioop import reverse

test=int(input())
while test:
    test-=1
    n=int(input())
    arr=list(map(int,input().split()))
    max_val=max(arr[1:n-1])
    tag=0
    for i in range(1,n-1):
        if arr[i]==max_val:
            tag=i
            break
    q=[]
    v=[0]*n
    for i in range(tag,0,-2):
        q.append((arr[i],i))
        v[i]=1
    for i in range(tag+2,n-1,2):
        q.append((arr[i],i))
        v[i]=1
    q.sort(reverse=True)
    p=[]
    for i in range(n):
        if not v[i]:
            p.append((arr[i],i))
    p.sort(reverse=True)
    p=p+q
    i=1
    for _,st in p:
        v[st]=i
        i+=1
    print(' '.join(map(str,v)))