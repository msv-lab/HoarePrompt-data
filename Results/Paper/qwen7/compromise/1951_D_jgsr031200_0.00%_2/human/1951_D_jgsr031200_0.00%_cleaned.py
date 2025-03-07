"""
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
 
 
# Read tree as graph
# Generic BS
def bs(arr,x):
    n = len(arr)
    l, r = 0, n - 1
    if x < arr[0]: return -1
    if x > arr[-1]: return n+1
 
    while l + 1 != r:
        mid = (l + r) // 2
        if x <= arr[mid]:
            r = mid
        else:
            l = mid
    return (l,r)
 
"""

def func_1(n, k):
    if n == k:
        print('YES')
        print(1)
        print(1)
        return
    if n < k:
        print('NO')
        return
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        h += curr
        n -= i * curr
    if h < k:
        print('NO')
    else:
        print(2)
        print('YES')
        print(*costs)
t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    func_1(n, k)