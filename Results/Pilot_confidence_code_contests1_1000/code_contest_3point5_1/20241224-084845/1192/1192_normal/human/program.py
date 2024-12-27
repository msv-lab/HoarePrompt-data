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
    def bfs(a,root):
      visited=[False]*(len(a)+1)
      queue=[root]
      visited[root]=True
      i=0
      while i<len(queue):
            vertex = queue[i]
            i+=1
            for w in a[vertex-1]:
                if not visited[w]:
                    visited[w]=True
                    queue.append(w)
      return queue       
     
    n,k=map(int, input().split())
    a=[]
    b=[0]*n
    c=[[] for i in range(n)]
    for i in range(k):
      l=list(map(int, input().split()))
      #del l[0]
      a.append(l)
     
    for i in range(k):
      if a[i][0]<2:
          continue
      for jj in range(2,a[i][0]+1):
        c[a[i][1]-1].append(a[i][jj])
        c[a[i][jj]-1].append(a[i][1])
        #for kk in range(jj+1,len(a[i])):
         # c[a[i][jj]-1].append(a[i][kk])
          #c[a[i][jj]-1].append(a[i][jj])
    #print(c)  
    for i in range(n):
      if b[i]==0:
        t=bfs(c,i+1)
        p=len(t)
        #print(t)
        for i in range(p):
          b[t[i]-1]=p
    for i in range(n):
      if b[i]==1:
        print(b[i],end=" ")
      else:
        print(b[i]-1,end=" ")    
if __name__ == '__main__':
    sync_with_stdio(False)
    main()