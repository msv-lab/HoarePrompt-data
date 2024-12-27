import os
import sys
import traceback

doprint='DOPRINT' in os.environ

ord9 = ord('9')
ord0 = ord('0')
ordA = ord('A')
def conv(d):
  ordd = ord(d)
  if ordd <= ord9: return ordd - ord0
  return 10 + ordd - ordA

def processds( ds):
  rtn = map( conv, list(ds))
  while rtn and not rtn[0]:
    if doprint: print( rtn )
    rtn.pop(0)
  return rtn

def solveone( ds, ub):
  if doprint: print( (ds,ub) )
  if len(ds) == 0: return [-1, -1]
  maxds = max(ds)
  if maxds > ub: return [0,0]
  if len(ds) == 1: return [-1,-1]
  lo = maxds + 1
  summ = 0
  for d in ds: summ = summ * lo + d
  if doprint: print( ('A',lo,summ,ub,summ>ub) )
  if summ>ub: return [0,0]
  hi = lo
  while True:
    hi += 1
    summ = 0
    for d in ds: summ = summ * hi + d
    if doprint: print( ('B',hi,summ,ub,summ>ub) )
    if summ>ub: return [lo,hi-1]

def solve():
  hs,ms = map( processds, sys.stdin.readline().strip('\n\r ').split(':') )

  if doprint: print( (hs,ms) )

  hminmax = solveone( hs, 23 )
  if hminmax[0]==0: return [0]
  mminmax = solveone( ms, 59 )
  if mminmax[0]==0: return [0]

  if hminmax[0]==-1 and mminmax[0]==-1: return [-1]
  if hminmax[0]==-1: return range(mminmax[0],mminmax[1]+1)
  if mminmax[0]==-1: return range(hminmax[0],hminmax[1]+1)
  if hminmax[0] > mminmax[1]: return [0]
  if mminmax[0] > hminmax[1]: return [0]
  return range(max([hminmax[0],mminmax[0]]), min([hminmax[1],mminmax[1]])+1 )

if __name__=="__main__":
  pfx=''
  for i in solve():
    sys.stdout.write( pfx+str(i) )
    pfx=' '
  sys.stdout.write( '\n' )
