import os
import sys
from atexit import register
from io import BytesIO
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
raw_input = lambda: sys.stdin.readline().rstrip('\r\n')

n = int(input())
ok = False
cont = 0
for i in xrange(n):
    a,b = (int(x) for x in input().split())
    if a == b:
        cont += 1
        if cont == 3:
            ok = True
    else:
        cont = 0
if ok:
    print("Yes")
else:
    print("No")