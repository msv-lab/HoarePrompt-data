t=int(input())
for _ in range(t):
    #n=int(input())
    n,q=map(int, input().split())
    #s=input()
    a=list(map(int, input().split()))
    
    ones=[0]
    for i in range(n):
        ones.append(ones[-1]+(a[i]==1))
    for i in range(q):
        l,r=map(int,input().split())
        if l==r:
            print("NO")
        else:
            if ones[r]-ones[l-1]>(r-l+1)/2:
                print("NO")
            else:
                # print(ones)
                print("YES")