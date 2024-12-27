import fractions
import sys
import math

def a( t1, t2, y1max, y2max, t0):
  dt1 = t0 - t1
  dt2 = t2 - t0

  if   dt1==0 and dt2==0: return y1max,y2max
  elif dt1==0: return y1max,0
  elif dt2==0: return 0,y2max

  calc1max = (y2max * dt2) / dt1
  if calc1max<y1max: y1max = calc1max

  if y1max < 1: return 0,y2max

  calc2max = (y1max * dt1 + dt2 - 1) / dt2
  if calc2max<y2max: y2max = calc2max

  if y1max*dt1 == y2max*dt2: return y1max,y2max

  if y1max==0: return 0,y2max

  if dt1<=y2max and dt2<=y1max:
    n = min( y1max/dt2, y2max/dt1)
    y1,y2 = n*dt2, n*dt1
    g = fractions.gcd( y1,y2)
    fr1,fr2 = y1/g, y2/g
    n = min( (y1max-y1)/fr1, (y2max-y2)/fr2)
    return y1+n*fr1, y2+n*fr2

  y1,y2 = y1max,y2max

  if y1<y2: d1,d2 = 1,0
  else    : d1,d2 = 0,1

  ###sys.stderr.write( str( dict(y1max=y1,y2max=y2,d1=d1,d2=d2,err=(y1*t1+y2*t2)/float(y1+y2)-t0))+'\n' )

  y1out,y2out = y1,y2
  errMin = (y1*t1+y2*t2)/float(y1+y2) - t0
  while y1>1 and y2>1:
    y1 -= d1
    y2 -= d2
    rem = y2*dt2 - y1*dt1
    if rem==0: return y1,y2
    if dt1 and rem>=dt2: y2 -= (rem/dt2)
    elif dt2 and rem<0: y1 -= (dt1-(rem+1))/dt1
    err = (y1*t1+y2*t2)/float(y1+y2) - t0
    ###print( (y1,y2,rem,err,errMin,) )
    if err<errMin: errMin,y1out,y2out = err,y1,y2

  return y1out,y2out


if __name__=="__main__":
  toks = sys.stdin.readline().split()
  t1 = int(toks[0])
  t2 = int(toks[1])
  y1max = int(toks[2])
  y2max = int(toks[3])
  t0 = int(toks[4])

  print( "%d %d" % a(t1,t2,y1max,y2max,t0) )
