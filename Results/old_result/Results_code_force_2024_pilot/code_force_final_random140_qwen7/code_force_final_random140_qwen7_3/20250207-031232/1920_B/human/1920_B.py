for _ in range(int(input())):
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    sum1 = sum(a)
    ans = []
    for i in range(k+1):
        if i==0:
            sums = sum1- 2*sum(a[:x+1])
            ans.append(sums)
        else:
            if i+x-1<n:
                sums = sums+a[i-1]-2*a[i+x-1]
                ans.append(sums)
            else:
                sums= sums+a[i-1]
                ans.append(sums)
    print(max(ans))