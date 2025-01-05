from __future__ import division, print_function
def main():
    def power(x, y, p) : 
        res = 1     # Initialize result 
    
        # Update x if it is more 
        # than or equal to p 
        x = x % p  
      
        while (y > 0) : 
              
            # If y is odd, multiply 
            # x with result 
            if ((y & 1) == 1) : 
                res = (res * x) % p 
     
            # y must be even now 
            y = y >> 1      # y = y/2 
            x = (x * x) % p 
              
        return res
    def count_next_smaller_elements(xs):
        ys = sorted((x,i) for i,x in enumerate(xs))
        zs = [0] * len(ys)
    
        for i in range(1, len(ys)):
            zs[ys[i][1]] = zs[ys[i-1][1]]
            if ys[i][0] != ys[i-1][0]: zs[ys[i][1]] += 1
        ts = [0] * (zs[ys[-1][1]]+1)
        us = [0] * len(xs)
    
        for i in range(len(xs)-1,-1,-1):
            x = zs[i]+1
            while True:
                us[i] += ts[x-1]
                x -= (x & (-x))
                if x <= 0: break
    
                x = zs[i]+1
            while True:
                x += (x & (-x))
                if x > len(ts): break
                ts[x-1] += 1

        return us
    mod=998244353
    n=int(input())
    l1=list(input().split())
    arr=[0]*10
    for item in l1:
        arr[len(item)-1]+=1
    ans=0
    for item in l1:
        for i in range(1,11):
            if arr[i-1]==0:
                continue
            x=len(item)
            res=0
            
            if x<=i:
                for j in range(x-1,-1,-1):
                    res=(res+int(item[j])*pow(10,(x-j-1)*2,mod))%mod
                    res=(res+int(item[j])*pow(10,(x-j)*2-1,mod))%mod
                ans=(ans+arr[i-1]*res)
            else :
                x-=1
                i-=1
                j=0
                while x>i:
                    res=(res+2*int(item[j])*pow(10,(x-i)+(2*(i+1))-1,mod))%mod
                    x-=1
                    j+=1

                i+=1
                x=len(item)
                for j in range(i-1,-1,-1):
                    res=(res+int(item[j+(x-i)])*pow(10,(i-j-1)*2,mod))%mod
                    res=(res+int(item[j+(x-i)])*pow(10,(i-j)*2-1,mod))%mod
                ans=(ans+arr[i-1]*res)
    print(ans)

######## Python 2 and 3 footer by Pajenegod and c1729

# Note because cf runs old PyPy3 version which doesn't have the sped up
# unicode strings, PyPy3 strings will many times be slower than pypy2.
# There is a way to get around this by using binary strings in PyPy3
# but its syntax is different which makes it kind of a mess to use.

# So on cf, use PyPy2 for best string performance.

py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange

import os, sys
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
import sys
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
            if s[i] >= b'0' [0]:
                numb = 10 * numb + conv(s[i]) - 48
            elif s[i] == b'-' [0]: sign = -1
            elif s[i] != b'\r' [0]:
                A.append(sign*numb)
                numb = zero; sign = 1
            i += 1
    except:pass
    if s and s[-1] >= b'0' [0]:
        A.append(sign*numb)
    return A

if __name__== "__main__":
  main()