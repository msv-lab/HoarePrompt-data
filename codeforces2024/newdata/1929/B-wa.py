for _ in range(int(input())):
    n,k=map(int,input().split())
    #l=list(map(int,input().split()))
    #l.sort()
    if k%2==0:
        if (k//2)%2==0:
            print(k//2)
        else:
            print(k//2+1)
    else:
        k=k+1
        print(k//2)
        