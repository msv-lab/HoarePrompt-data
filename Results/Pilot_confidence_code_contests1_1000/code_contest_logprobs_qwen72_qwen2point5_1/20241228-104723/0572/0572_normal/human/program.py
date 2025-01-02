from __future__ import division, print_function
import bisect
import math
import itertools
import sys
from atexit import register
 
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream
 
 
if sys.version_info[0] < 3:
    class dict(dict):
        """dict() -> new empty dictionary"""
        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)
 
        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)
 
        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)
 
    input = raw_input
    range = xrange
 
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
 
 
def sync_with_stdio(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.
 
    Args:
        sync (bool, optional): The new synchronization setting.
 
    """
    global input, flush
 
    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip('\r\n')
 
        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
 
def main():
    n=int(input()) 
    a=list(map(int, input().split()))
    k=int(input())
    m=-1
    ma=0
    c=[]
    for i in range(k):
      b=list(map(int, input().split()))
      if b[0]==2:
        if b[1]>=m:
          m=b[1]
          ma=i
      c.append(b)
    p=0
    #print(m,ma,c)
    for i in range(ma):
      if c[i][0]==1:
        a[c[i][1]-1]=c[i][2]      
    for i in range(k-1,ma-1,-1):
      if c[i][0]==1 and p==0:
        continue
      if c[i][0]==2 :
        x=c[i][1]
        p=1 
      if c[i][0]==1 and p==1:
        c[i][2]=max(x,c[i][2])
    for i in range(n):
      if a[i]<m and m!=-1:
        a[i]=m
    
    for i in range(ma,k):
      if c[i][0]==1:
        a[c[i][1]-1]=c[i][2]
    print(*a)


 
        
if __name__ == '__main__':
    sync_with_stdio(False)
    main()