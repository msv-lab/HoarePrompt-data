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
    n, x = (int(q) for q in input().split())
    lst = [int(q) for q in input().split()]
    ans_min = (sum(lst)+x-1)//x
    ans_max = sum([(val+x-1)//x for val in lst])
    print("{} {}".format(ans_min, ans_max))