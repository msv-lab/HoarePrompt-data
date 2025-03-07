#     main()
T=int(input())
for _ in range(T):
    n,x,y=map(int,input().split())
    list0=list(map(int,input().split()))
    list0=sorted(list0)
    count=0
    for i in range(x-1):
            num=list0[i+1]-list0[i]-1
            if num==1:
                count+=1
    num=(list0[0]+n)-(list0[-1])-1
    if num==1:
        count+=1
    print(count+x-2)