n=int(input())
v=[]
t=[]
p=0
z=0
for j in range (0,n):
    a, b = map(int, raw_input().split())
    t.append (a)
    p=p+b
    v.append(b)
    z=z+a
    

    
def minpay(p,z,i):
    if i<0:
        return p
    else:
        if z>=1:
            return min(minpay(p+v[i],z+t[i],i-1), minpay(p,z-1,i-1))
        else:
            return minpay(p+v[i],z+t[i],i-1)
    
print (minpay(0,0,n-1))        
        

        
    
    
