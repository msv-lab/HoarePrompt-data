h, n  = map(int, raw_input().split())
l = map(int, raw_input().split())

mneg = 0
som = 0
neg = 0

for i in xrange(n):
    if(l[i] < 0):
        neg += l[i]
    else:
        if(neg < mneg):
            mneg = neg
        neg = 0
    som += l[i]

if(neg < mneg):
    mneg = neg

if(mneg*-1 > h):
    li = h
    for i in xrange(n):
        li += l[i]
        if(li <= 0):
            break
    print(i+1)
elif(som < 0):
    li = h - (h/(som*-1)-1)*(som*-1)
    for i in xrange(n):
        li += l[i]
        if(li <= 0):
            break
    print((h/(som*-1)-1)*n+i+1)
else:
    print("-1")