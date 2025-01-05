for i in range(int(input())):
    n,a,b=map(int,input().split())
    k = min(n, max(0, b-a))
    print(a*n + (b-a)*k - k*(k-1)//2)
