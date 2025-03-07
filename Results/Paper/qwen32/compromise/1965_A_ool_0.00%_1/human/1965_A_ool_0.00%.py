import heapq
import sys
 
input = sys.stdin.readline
 
def solve(arr):
    A = False
    if arr[0] != 1:
        return 'Alice'
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i-1] > 1:
            not_c = False
            break
        A = not A
    if not_c:
        A = not A
 
    return 'Alice' if A else 'Bob'
 
 
t = int(input())
c = 1
while t > 0:
    n = list(map(int, input().rstrip().split()))
 
    arr = list(map(int, input().rstrip().split()))
    r = solve(arr)
    print(r)
    t -= 1