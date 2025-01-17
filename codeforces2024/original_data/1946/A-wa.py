for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    if n%2==0:
        m = (n//2)-1
    else:
        m = n//2
    a[m]+=1
    if n==1:
        print(1)
    elif a[m-1]<=a[m] and a[m]<=a[m+1] :
        print(1)
    elif a[m]>a[m+1]:
        cnt = 1
        while m+1<n and a[m+1]<a[m]:
            a[m+1]+=1
            m+=1
            cnt+=1
        print(cnt)