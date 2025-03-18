def solve():
    n = int(input())
    v =[0]*(n + 1)
    v = [0] + list(map(int, input().split()))
    if n==2:
        print(2)
    else:
        for i in range(1,n+1):
            if v[v[v[i]]]==i:
                print(2)
                return
        print(3)
 
t = int(input())
for i in range(t):
    solve()