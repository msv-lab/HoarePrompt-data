t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    lst=[]
    for i in arr:
        lst.append(i)
    lst.sort()
    first=lst[0]
    for i in range (n):
        if arr[i]==first:
            index=i
            break
    j=0
    flag=True
    while j<n:
        if lst[j]==arr[index%n]:
            pass
            
            
            
        else:
            flag=False
            break
        j+=1
        index+=1
    if flag==True:
        print("YES")
    else:
        print("NO")