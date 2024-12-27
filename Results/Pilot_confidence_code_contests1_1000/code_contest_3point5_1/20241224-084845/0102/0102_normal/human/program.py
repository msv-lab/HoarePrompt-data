import os
import sys
from atexit import register
from io import BytesIO
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
raw_input = lambda: sys.stdin.readline().rstrip('\r\n')

for _ in xrange(int(input())):
    s = list(input().strip())
    n = len(s)
    lst1 = [0 for _ in range(n)]
    lst = [0 for _ in range(n)]

    ans = 0
    for i in range(1,n-1):
        if s[i+1] == s[i-1] == s[i]:
            s[i] = ans
            s[i+1] = ans + 1
            ans += 2
    for i in range(1,n-1):
        if s[i-1] == s[i+1]:
            s[i+1] = ans
            ans += 1
    for i in range(1,n):
        if s[i] == s[i-1]:
            s[i] = ans
            ans += 1

    print(ans)