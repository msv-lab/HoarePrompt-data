from __future__ import division, print_function
from itertools import permutations 
import threading,bisect,math,heapq,sys
from collections import deque
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
def dfs(n,d,v):
    v[n]=1
    x=d[n]
    for i in x:
        if i not in v:
            dfs(i,d,v)
    return p 
"""**************************MAIN*****************************"""
def main():
    def f(x,a):
        b=0
        mx=0
        mi=0
        for i in range(len(a)):
            b+=a[i]-x
            mx=max(b,mx)
            mi=min(b,mi)
        ans=mx-mi
        return ans
    n=inin()
    a=ain()
    l=-100005
    r=100005
    h=101
    ans=i_m
    while(h>0):
        h-=1
        m1=l+(r-l)/3
        m2=r-(r-l)/3
        p=f(m1,a)
        q=f(m2,a)
        ans=min(p,q,ans)
        if p<=q:
            r=m2
        else:
            l=m1
    print(ans)

"""***********************************************"""
def block(x): 
      
    v = []  
    while (x > 0): 
        v.append(int(x % 2)) 
        x = int(x / 2) 
    ans=[]
    for i in range(0, len(v)): 
        if (v[i] == 1): 
            ans.append(2**i)  
    return ans 
def intersection(l,r,ll,rr):
    # print(l,r,ll,rr)
    if (ll > r or rr < l): 
            return -1  
    else: 
        l = max(l, ll) 
        r = min(r, rr)
    return max(0,r-l) 
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