from __future__ import division, print_function
import bisect
import math
import heapq
import itertools
import sys
from collections import deque
from atexit import register
from collections import Counter
from functools import reduce
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
    # sys.stdin  = open("input.txt")
    def dijkstra(n, s, edges):
        hq = [(0, s)]
        cost = [float('inf')] * n
        cost[s] = 0
        while hq:
            c, v = heapq.heappop(hq)
            if c > cost[v]:
                continue
            for d, u in edges[v]:
                tmp = d + cost[v]
                if tmp < cost[u]:
                    cost[u] = tmp
                    heapq.heappush(hq, (tmp, u))
        return cost[-1]

    n,m=map(int,input().split())
    sx, sy, fx, fy = map(int, input().split())
    xy=[None]*m
    for i in range(m):
        xy[i]=list(map(int,input().split()))
        xy[i].append((i+1))
    adj=[[] for i in range(m+2)]
    xy.sort()
    for i in range(m-1):
        dist=min(abs(xy[i][0]-xy[i+1][0]),abs(xy[i][1]-xy[i+1][1]))
        adj[xy[i][2]].append([dist,xy[i+1][2]])
        adj[xy[i+1][2]].append([dist,xy[i][2]])
    xy.sort(key= lambda x:x[1])
    for i in range(m-1):
        dist=min(abs(xy[i][0]-xy[i+1][0]),abs(xy[i][1]-xy[i+1][1]))
        adj[xy[i][2]].append([dist,xy[i+1][2]])
        adj[xy[i+1][2]].append([dist,xy[i][2]])
    for x,y,i in xy:
        d1= min(abs(x-sx),abs(y-sy))
        d2=abs(x-sx)+abs(y-sy)
        adj[0].append([d1,i])
        adj[i].append([d2,0])
        d1= min(abs(x-fx),abs(y-fy))
        d2=abs(x-fx)+abs(y-fy)
        adj[m+1].append([d1,i])
        adj[i].append([d2,m+1])
    d=abs(sx-fx)+abs(sy-fy)
    adj[0].append([d,m+1])
    adj[m+1].append([d,0])
    print(dijkstra(m + 2, 0, adj))
    
if __name__ == '__main__':
    sync_with_stdio(False)
    main()