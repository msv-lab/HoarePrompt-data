from math import log, ceil

k,b,n,t = map(int, raw_input('').split(' '))
if k!=1:
    c = k**(n-1)*(k-1+b)-b
    if t*(k-1) >= c:
        i = 0
    else:
        #i = ceil(log(c+1, k))
        i = log(c+b, k) - log(t*(k-1)+b, k) + 1
        '''i = int(i)
        amount = k**(i-1)*(t+b/float(k-1))-b/float(k-1)
        while amount < z:
            i += 1
            amount = k**(i-1)*(t+b/float(k-1))-b/float(k-1)'''
else:
    z = k+b*(n-1)
    if t >= z:
        i = 0
    else:
        i = int((z-t)/float(b) + 1)
        amount = t+b*(i-1)
        while amount < z:
            i += 1
            amount = t+b*(i-1)

#print(i)
print(int(ceil(i)))