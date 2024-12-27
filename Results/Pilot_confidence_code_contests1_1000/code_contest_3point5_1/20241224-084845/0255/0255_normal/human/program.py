from __future__ import print_function,division
import sys
if sys.version_info < (3, 0):
    range = xrange
input = sys.stdin.readline

n = int(input())

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

DP = [0]*2*(n+1)

roundwina = 0
t = 1
sa = 0
for a in A[1:]:
    roundwina += t*a
    sa += a
    t += 1
for b in reversed(B[1:]):
    roundwina += t*b
    sa += b
    t += 1

roundwinb = 0
sb = 0
t = 1
for b in B[1:]:
    roundwinb += t*b
    sb += b
    t += 1
for a in reversed(A[1:]):
    roundwinb += t*a
    sb += a
    t += 1

top = True
best = 0
win = 0
i = 0

#print('round',roundwina,roundwinb)
for t in range(2*n):
    if top:
        win += t*A[i]
        endnow = win + roundwina + t*sa
        if t%2 == 0:
            endnow += (2*n-1)*B[i]
    else:
        win += t*B[i]
        endnow = win + roundwinb + t*sb
        if t%2 == 0:
            endnow += (2*n-1)*A[i]

    if t%2 == 1:
        i += 1
        if i != n:
            #print(A[i],B[i])
            #print('summa',sa,sb)
            #print(2*(n-i-1)*A[i])
            #print(2*(n-i-1)*B[i])
            roundwina -= sa + (2*(n-i)-1)*B[i]
            roundwinb -= sb + (2*(n-i)-1)*A[i]
            sa -= A[i] + B[i]
            sb -= A[i] + B[i]
        #print('round',roundwina,roundwinb)
    else:
        top = not top

    best = max(best, endnow)
best = max(win,best)

print(best)
