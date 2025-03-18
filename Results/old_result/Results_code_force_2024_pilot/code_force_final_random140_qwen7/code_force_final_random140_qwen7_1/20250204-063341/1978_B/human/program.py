t = int(input())
while t:
    x = list(map(int,input().split(" ")))
    n = x[0]
    a = x[1]
    b = x[2]
    profit = n*a
    if a >= b:
        print(profit)
    else:
        k = b-a
        k = min(n-1,k)
        profit = profit + (b-a)*(k+1) - (k*(k+1))/2
        
        print(int(profit))
    
    t-=1