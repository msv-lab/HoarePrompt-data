t=int(input())
for i in range(t):
    n=int(input())
    l=map(int,input().split())
    lis=sorted(set(l))
    if (1 not in lis) or (len(lis)==1) :
        print("Alice")
    else:
        
        test=True
        for j in range(1,len(lis)):
            if lis[j]-lis[j-1]>1:
                if j%2==1:
                    print("Bob")
                else:
                    print("Alice")
                test=False
                break
        if test==True:
            if len(lis)%2==1:
                print("Alice")
            else:
                print("Bob")