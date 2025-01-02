def counts(a, b, c, l):
    res=0
    lb = max(a, b+c)
    ub = a+l
    for i in xrange(lb, ub+1):
        temp = i-a
        x = min(a-b-c+temp, l-temp)
        if x>=0:
            res += ((x+1)*(x+2))/2
    return res

a, b, c, l = map(int, raw_input().split())
print ((l+1)*(l+2)*(l+3))/6 - counts(a, b, c, l) - counts(b, a, c, l) - counts(c,a , b, l)