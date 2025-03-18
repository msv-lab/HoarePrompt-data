def jewels():
    n, k = map(int, input().split())
    if n<k:
        print("NO")
    elif n == k:
        print("YES")
        print(1)
        print(1)
    elif k-1<n-k+1:
        print("YES")
        print(2)
        print(n-k+1, 1)
    else:
        print("NO")
 
for _ in range(int(input())):
    jewels()