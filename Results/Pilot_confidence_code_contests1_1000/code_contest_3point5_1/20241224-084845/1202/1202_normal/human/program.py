from fractions import Fraction,gcd
from sys import stdin,stdout
for _ in xrange(input()):
    n=input()
    s=stdin.readline()
    d={}
    a,b=0,0
    ans=""
    for i in s:
        if i=="D":
            a+=1
        elif i=="K":
            b+=1
        else:
            break
        if a!=0 and b!=0:
            x=gcd(a,b)
            x=str(a/x)+" "+str(b/x)
            try:
                d[x]+=1
                ans+=str(d[x])+" "
            except:
                d[x]=1
                ans+="1 "
        else:
            ans+=str(max(a,b))+" "
    stdout.write(ans+"\n")