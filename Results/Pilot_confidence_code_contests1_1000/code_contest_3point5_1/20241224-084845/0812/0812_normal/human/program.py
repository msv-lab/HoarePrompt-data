import sys
import math
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
a = [0]*n
for i in range(n):
  a[i] = int(sys.stdin.readline())

asort = sorted(a, reverse=True)

numspacesremaining = asort[0]*(n-1) - sum(asort[1:])

if m <= numspacesremaining:
  mink = max(asort)
else:
  mink = max(asort) + max(math.ceil((m - numspacesremaining)/float(n)), 0)

maxk = max(a) + m

print(str(int(mink)) + " " + str(maxk))
