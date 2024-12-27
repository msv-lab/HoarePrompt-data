from __future__ import division, print_function
import threading,bisect,math,heapq,sys
# threading.stack_size(2**27)
# sys.setrecursionlimit(10**4)
from sys import stdin, stdout
i_m=9223372036854775807    
def cin():
    return map(int,sin().split())
def ain():                           #takes array as input
    return list(map(int,sin().split()))
def sin():
    return input()
def inin():
    return int(input()) 
prime=[]
def dfs(n,d,v,a,c):
    v[n]=1
    if n in d:
        x=d[n]
    else:
        a[n]+=c
        x=[]
    p=a[n]
    for i in x:
        if i not in v:
            dfs(i,d,v,a,c)
            p+=a[i]
    a[n]=p
    return p

"""**************************MAIN*****************************"""
def main():
    def fun(s,p):
        lpm=[]
        hpm=[]
        if p==1:
            s=s[::-1]
        a=c=1000000000
        b=d=-1000000000
        for i in s:
            if p==1:
                lpm.append((a,c))
                hpm.append((b,d))
            a=min(a,i[0])
            b=max(b,i[0])
            c=min(c,i[1])
            d=max(d,i[1])
            if p==0:
                lpm.append((a,c))
                hpm.append((b,d))
        if p==1:
            lpm=lpm[::-1]
            hpm=hpm[::-1]
        return lpm,hpm
    t=inin()
    for _ in range(t):
        s=sin()
        a=[]
        x=y=0
        p=q=1
        for i in s:
            if i=="W":
                x+=1
                p=2
            elif i=="S":
                x-=1
                p=2
            elif i=="A":
                y-=1
                q=2
            else:
                y+=1
                q=2
            a.append((x,y))
        lpm,hpm=fun(a,0)
        lsm,hsm=fun(a,1)
        n=len(s)
        x=i_m
        y=i_m
        for i in range(n):
            a,b,c,d=lpm[i][0],lsm[i][0],hpm[i][0],hsm[i][0]
            x=min(x,max(c,d,0)-min(a,b,0))
            y=min(y,max(c,d-1,0)-min(a,b-1,0),max(c,d+1,0)-min(a,b+1,0))
        xx=i_m
        yy=i_m
        for i in range(n):
            a,b,c,d=lpm[i][1],lsm[i][1],hpm[i][1],hsm[i][1]
            xx=min(xx,max(c,d,0)-min(a,b,0))
            yy=min(yy,max(c,d-1,0)-min(a,b-1,0),max(c,d+1,0)-min(a,b+1,0))
        # print(lpm,hpm,lsm,hsm)

        x=max(x+1,p)
        y=max(y+1,p)
        xx=max(xx+1,q)
        yy=max(yy+1,q)
        ans=min(x*xx,x*yy,y*xx)
        print(ans)


"""*******************************************************"""

######## Python 2 and 3 footer by Pajenegod and c1729
fac=[]
def fact(n,mod):
    global fac
    fac.append(1)
    for i in range(1,n+1):
        fac.append((fac[i-1]*i)%mod)
    f=fac[:]
    return f
def nCr(n,r,mod):
    global fac
    x=fac[n]
    y=fac[n-r]
    z=fac[r]
    x=moddiv(x,y,mod)
    return moddiv(x,z,mod)
def moddiv(m,n,p):
    x=pow(n,p-2,p)
    return (m*x)%p
def GCD(x, y): 
    x=abs(x)
    y=abs(y)
    if(min(x,y)==0):
        return max(x,y)
    while(y): 
        x, y = y, x % y 
    return x 
def Divisors(n) : 
    l = []  
    ll=[]
    for i in range(1, int(math.sqrt(n) + 1)) :
        if (n % i == 0) : 
            if (n // i == i) : 
                l.append(i) 
            else : 
                l.append(i)
                ll.append(n//i)
    l.extend(ll[::-1])
    return l
def SieveOfEratosthenes(n): 
    global prime
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    f=[]
    for p in range(2, n): 
        if prime[p]: 
            f.append(p)
    return f
def primeFactors(n): 
    a=[]
    while n % 2 == 0: 
        a.append(2) 
        n = n // 2 
    for i in range(3,int(math.sqrt(n))+1,2):  
        while n % i== 0: 
            a.append(i) 
            n = n // i  
    if n > 2: 
        a.append(n)
    return a
"""*******************************************************"""
py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange
import os
from io import IOBase, BytesIO
BUFSIZE = 8192
class FastIO(BytesIO):
    newlines = 0
 
    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.writable = "x" in file.mode or "w" in file.mode
        self.write = super(FastIO, self).write if self.writable else None
 
    def _fill(self):
        s = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
        self.seek((self.tell(), self.seek(0,2), super(FastIO, self).write(s))[0])
        return s
 
    def read(self):
        while self._fill(): pass
        return super(FastIO,self).read()
 
    def readline(self):
        while self.newlines == 0:
            s = self._fill(); self.newlines = s.count(b"\n") + (not s)
        self.newlines -= 1
        return super(FastIO, self).readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.getvalue())
            self.truncate(0), self.seek(0)
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        if py2:
            self.write = self.buffer.write
            self.read = self.buffer.read
            self.readline = self.buffer.readline
        else:
            self.write = lambda s:self.buffer.write(s.encode('ascii'))
            self.read = lambda:self.buffer.read().decode('ascii')
            self.readline = lambda:self.buffer.readline().decode('ascii')
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip('\r\n') 
# Cout implemented in Python
class ostream:
    def __lshift__(self,a):
        sys.stdout.write(str(a))
        return self
cout = ostream()
endl = '\n'
 
# Read all remaining integers in stdin, type is given by optional argument, this is fast
def readnumbers(zero = 0):
    conv = ord if py2 else lambda x:x
    A = []; numb = zero; sign = 1; i = 0; s = sys.stdin.buffer.read()
    try:
        while True:
            if s[i] >= b'R' [0]:
                numb = 10 * numb + conv(s[i]) - 48
            elif s[i] == b'-' [0]: sign = -1
            elif s[i] != b'\r' [0]:
                A.append(sign*numb)
                numb = zero; sign = 1
            i += 1
    except:pass
    if s and s[-1] >= b'R' [0]:
        A.append(sign*numb)
    return A
 
# threading.Thread(target=main).start()
if __name__== "__main__":
  main()