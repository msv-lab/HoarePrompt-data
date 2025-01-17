import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(100000)  # Example limit

t = int(input())
for _ in range(t) :
    n = int(input())
    a = input()[::1]
    b = input()[::1]
    
    mn = pow(2, n+1) - 1

    l = list()
    if (a[0] == '1') :
        l.append(1)
    else :
        l.append(0)

    for i in range(1, n):
        if a[i] == '1':
            l.append(pow(2, i) + l[i-1])
        else :
            l.append(l[i-1])
    
    l = l[::1]
    #print(l)

    l2 = list()
    if (b[0] == '1') :
        l2.append(2)
    else :
        l2.append(0)

    for i in range(1, n):
        if b[i] == '1':
            l2.append(pow(2, i+1) + l2[i-1])
        else :
            l2.append(l2[i-1])
    
    l2 = l2[::1]
    
    #print(l2)

    ind = 0

    for i in range(0, n):
        cnt = l[i] + l2[n-1]
        if (i > 0):
            cnt -= l2[i-1]
        
        if (cnt < mn) :
            mn = cnt
            ind = i

    s = ""
    for i in range(0, n):
        if (i <= ind):
            s += a[i]
        if (ind <= i):
            s += b[i]

    ans = 0
    for i in range(0, n):
        cnt = l[i] + l2[n-1]
        if (i > 0):
            cnt -= l2[i-1]
        
        if (cnt == mn) :
            #print(i)
            ans += 1
   # print(mn)
    print(s)
    print(ans)