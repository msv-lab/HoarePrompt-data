a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    if (b>=c and b%2==c%2):
        print("YES")
    else:
        print("NO")