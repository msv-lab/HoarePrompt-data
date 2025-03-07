# sterlin
import sys
input = lambda: sys.stdin.readline().rstrip()
 
def ii():
    return int(input())
 
def mi():
    return map(int, input().split())
 
def li():
    return list(map(int, input().split()))
 
def si():
    return input()
 
def lsi():
    return input().split()
 
 
 
t = ii()
for _ in range(t):
    n, x = mi()
    p = li()
 
    num_indx = {num: indx + 1 for indx, num in enumerate(p)}
    seen = [0]*n
    left = 0
    right = n
    
 
    while left + 1 < right:
        mid = left + (right - left)//2
 
        seen[p[mid] - 1] = 1
        if p[mid] <= x:
            left = mid
        
        else:
            right = mid
    
 
    if p[left] == x:
        print(0)
    
    elif not seen[x - 1]:
        print(1)
        print(left + 1, num_indx[x])
    else:
        seen[p[left] - 1] = 0
        temp = sorted([indx + 1 for indx, vis in enumerate(seen) if not vis])
        print(2)
        print(num_indx[temp[0]], num_indx[x])
        print(num_indx[temp[0]], left + 1)