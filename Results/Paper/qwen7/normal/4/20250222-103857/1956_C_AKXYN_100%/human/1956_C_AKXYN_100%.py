for _ in range(int(input())):
    n=int(input())
    mat=[list(range(1,n+1)) for i in range(n)]
    res=0
    for i in range(n):
        res+=(i+1)*(2*i+1)
    print(res,n<<1)
    for i in range(n,0,-1):
        print("1 %d"%i,*range(1,n+1))
        print("2 %d"%i,*range(1,n+1))