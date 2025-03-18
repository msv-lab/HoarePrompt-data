import math as m
for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    s = list(map(int,input().split()))
    s[0],s[k-1] = s[k-1],s[0]
    ans = 0
    h = s[0]
    j = -1
    for i in s[1:]:
        j += 1
        if h<i:
            break
        else:
            ans += 1
    p = j
    s[0],s[k-1] = s[k-1],s[0]
    ans1 = 0
    s[p],s[k-1] = s[k-1],s[p]
    z = 0
    for i in s:
        if i==h:
            if s[0]!=h:
                ans1 += 1
            z = 1
        elif i>h:
            break
        else:
            if z==1:
                ans1 += 1
    print(max(ans,ans1))