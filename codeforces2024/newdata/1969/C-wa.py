t = int(input())

for _ in range(t):

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if(n==1):
        print(a[0])
        continue

    for i in range(k):
        diff, ind = 0, 0

        for j in range(1, n):
            # print(j, abs(a[j]-a[j-1]), diff)
            if(abs(a[j]-a[j-1])>diff):
                diff = abs(a[j]-a[j-1])
                ind = j
        
        # print("-=-=", diff, ind)
        if(a[ind]>a[ind-1]):
            a[ind] = a[ind-1]
        else:
            a[ind-1] = a[ind]

        # print(i, "-->", a)
    
    print(sum(a))
