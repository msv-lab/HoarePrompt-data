import os
a = str(raw_input())
k = int(raw_input())
la = len(a)
i = la -1
judge = True
if k >= la:
    judge = False
    print (la + k)/2*2
while i >= 0 and judge:
    if a[i:la] in a[0:i-k+1]:
        i -= 1
    else:
        break
if judge:
    print (la - i - 1  + k)/2*2*2