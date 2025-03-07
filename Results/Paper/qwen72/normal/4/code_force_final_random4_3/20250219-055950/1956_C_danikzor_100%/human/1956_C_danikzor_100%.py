def solve():
    n = int(input())
    print(n*(n+1)*(4*n-1)//6, 2*n)
    for i in range(1, n+1):
        print(1, i, *range(n, 0, -1))
        print(2, i, *range(n, 0, -1))
 
 
t = int(input())
for t in range(t, 0, -1):
    solve()