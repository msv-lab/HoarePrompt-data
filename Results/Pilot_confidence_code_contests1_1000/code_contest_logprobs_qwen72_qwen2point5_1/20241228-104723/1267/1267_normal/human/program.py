import sys
import math

n = input()
a = map(int, raw_input().split())
a.reverse()

for i in xrange(n) :
    sys.stdout.write(str(a[i]))
    if i < n-1 :
        sys.stdout.write(" ")
print