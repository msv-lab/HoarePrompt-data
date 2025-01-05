def gcd(x,y):
    if x>=y:
        if x%y==0:
            return y
        else:
            return gcd(y,x%y)
    else:
        if y%x==0:
            return x
        else:
            return gcd(x,y%x)
def gcd2(x4):
    if len(x4)>2:
        return gcd2([gcd(x4[0],x4[1]),]+x4[2:])
    elif len(x4) ==2:
        return gcd(x4[0],x4[1])
    else:
        return x4[0]
N, X = map(int,input().split())
x=[int(i) for i in input().split()]
x.append(X)
x3=[]
for i in range(len(x)-1):
    x3.append(abs(x[i+1]-x[i]))
print(gcd2(x3))
