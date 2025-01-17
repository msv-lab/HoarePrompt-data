for _ in range(int(input())):
    n,x = map(int,input().split())
    a= [0]+ list(map(int,input().split()))
    l = 1
    r = n+1
    mid = (l+r)//2
    if a[mid] == x:
        print(0)
    else:
        print(1)
        print(mid,n)