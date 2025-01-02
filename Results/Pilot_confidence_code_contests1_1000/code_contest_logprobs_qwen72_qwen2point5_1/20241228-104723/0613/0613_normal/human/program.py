from sys import stdin, stdout
from collections import Counter
cin, cout = stdin.readline, stdout.write
size = int(cin())
array = map(int, cin().split())
check = Counter(array)
possible = True
inc, dec = list(), list()
for num in check:
    if check[num]>2: 
        possible = False
        break
    elif check[num]==2:
        inc.append(num)
        dec.append(num)
    else: inc.append(num)
if possible:
    cout("Yes\n")
    inc.sort()
    dec.sort(reverse = True)
    cout("%d\n"%len(inc))
    for i in xrange(len(inc)): cout("%d "%inc[i])
    cout("\n%d\n"%len(dec))
    for i in xrange(len(dec)): cout("%d "%dec[i])
    cout("\n")
else: cout("No\n")




