import math
n,k = map(int, raw_input().split())
a =  map(int, raw_input().split())
mx = n / a[0]
idx = 1
lasteq = math.floor(n / a[0] * 1.0) * a[0]
for i in range(1,k):
    eq = math.floor(n / a[i] * 1.0) * a[i]
    if eq > lasteq :
        lasteq = eq
        mx = n/a[i]
        idx = i+1
    elif eq == lasteq:
      b1 = n / a[i]
      if b1 < mx :
          mx = b1
          idx = i+1
print("%d %d" % (idx, mx)) 