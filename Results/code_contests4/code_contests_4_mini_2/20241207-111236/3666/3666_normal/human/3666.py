from __future__ import division, print_function
 
import os,sys
from io import BytesIO, IOBase
 
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
 
 
def ii():  return int(input())
def si():  return input()
def mi():  return map(int,input().split(" "))
def msi(): return map(str,input().split(" "))
def li():  return list(mi())
 
def dmain():
    sys.setrecursionlimit(1000000)
    threading.stack_size(1024000)
    thread = threading.Thread(target=main)
    thread.start()
    
import math
def getSum(n): 
    sum = 0
    while(n > 0): 
        sum += int(n%10) 
        n = int(n/10) 
  
    return sum

def isPowerOfTwo (x): return (x and (not(x & (x - 1))) )
 
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
def egcd(a, b):  
    if a == 0 :   
        return b, 0, 1
    gcd, x1, y1 = egcd(b%a, a)
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd, x, y 
    
def checkPrime(n) : # Check Prime Number or not 
    if (n <= 1) : return False
    if (n <= 3) : return True
    if (n % 2 == 0 or n % 3 == 0) : return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
def fib(n):
    if n==0:
        return (0,1)
    p=fib(n>>1)
    c=p[0]*(2*p[1]-p[0])
    d=p[0]*p[0]+p[1]*p[1]
    if (n&1):
        return c+2*d 
    else:
        return c+d 
def read():
    sys.stdin = open('input.txt', 'r')  
def powLog(x,y):
    res=1
    while y>0:
        if y&1:
            res=res*x
        x=x*x
        y>>=1
    return res
def main():
    q=ii()
    for i in range(q):
        l1,r1,l2,r2=mi()
        print(l1,r2)

# region fastio
# template taken from https://github.com/cheran-senthil/PyRival/blob/master/templates/template.py
 
BUFSIZE = 8192
 
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()
 
 
if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
 
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# endregion
 
 
if __name__ == "__main__":
    #read()
    main()
    #dmain()
 
# Comment Read()