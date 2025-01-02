import sys,math
from collections import defaultdict
from io import BytesIO

sys.stdin = BytesIO(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')
n = int(input())
arr = [int(x) for x in input().split(' ')]
#n,k = map(int, input().split(' '))
#print(arr)

#print(arr)
h = max(arr)
res = list()
for el in arr:
    if len(res) == 0 or res[-1] != el:
        if len(res) > 0:
            if res[-1] < el:
                print('NO')
                exit()
        res.append(el)
    else:
        res.pop()
if len(res) > 1:
    print('NO')
elif len(res) == 0:
    print('YES')
else:
    print('NO' if res[-1] < h else 'YES')
