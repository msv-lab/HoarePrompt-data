for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a=[abs(x) for x in a]
    print(sum(a))
    
