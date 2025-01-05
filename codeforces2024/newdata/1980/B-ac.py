t=int(input())
for _ in range(t):
    n,f,k=map(int,input().split())
    a=list(map(int,input().split()))
    special=a[f-1]
    a.sort(reverse=True)
    b=[]
    c=[]
    for i in range(k):
        b.append(a[i])
    for i in range(k,n):
        c.append(a[i])
    if special in b and special in c:
        print("MAYBE")
    elif special in b and special not in c:
        print("YEs")
    elif special in c and special not in b:
        print("No")