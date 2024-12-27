import heapq
import sys
import unittest

def dist(seg):
    return (seg[0][0]-seg[1][0])**2 + (seg[0][1]-seg[1][1])**2

def dosolve(inf):   
    points = []
    ret = []
    for i in range(4):
        x,y,x1,y1 = map(int,inf.readline().split())
        f,t = [x,y],[x1,y1]
        points.append(f)
        points.append(t)
        ret.append([f,t])
    points.sort()
    #print 'Points:%s' % points
    #print 'Ret:%s' % ret
    for i in range(4):
        if points[2*i] != points[2*i+1]: return 'NO'
    #print 'p2\n'
    m = [dist(d) for d in ret]
    m.sort()
    if m[0] != m[1]: return 'NO'
    if m[2] != m[3]: return 'NO'
    #print 'p3\n' 
    if m[0] == 0: return 'NO'
    #
    #for r in ret:
    #    if dist(r) != d: 
    #        print 'D:%s' % ((r,dist(r)),)
    #        return 'NO'
    #print 'p4\n'
    if dist([points[0],points[4]]) != dist([points[2],points[6]]): return 'NO'
    #print 'p5\n'
    return 'YES'

def solvecase(inf,outf):
    outf.write('%s\n' % dosolve(inf))

if __name__=="__main__":
    solvecase(sys.stdin,sys.stdout)
