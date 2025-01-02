import fractions
import sys
import math

P='perim'
L='length'
W='width'
H='height'
C='cost'

def b( rs, ws):
  rtn = 0
  for r in rs:
    mx = 1000000000
    for w in ws:
      if w[L] < r[P]: continue
      wpw = (w[L] / r[H] ) *  w[W]
      mx = min( mx, w[C] * ((r[P] + wpw -1 ) / wpw) )
    rtn += mx
  return mx

if __name__=="__main__":
  nr = int(sys.stdin.readline().split()[0])
  rs= []
  for i in range(nr):
    toks = sys.stdin.readline().split()
    rs += [ { P:2*(int(toks[0]) + int(toks[1])), H:int(toks[2]) } ]

  nw = int(sys.stdin.readline().split()[0])
  ws= []
  for i in range(nw):
    toks = sys.stdin.readline().split()
    ws += [ { L:int(toks[0]), W:int(toks[1]), C:int(toks[2]) } ]
  
  print( "%d" % b(rs, ws) )
