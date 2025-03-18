def ii(): return int(input())
 
def mii(): return map(int, input().split())
 
def lii(): return list(map(int, input().split()))
 
def slii(): return sorted(list(map(int, input().split())))
 
def mis(): return map(str, input().split())
 
def lis(): return list(input())
 
def slis(): return sorted(list(map(str, input().split())))
 
def pre(arr):
    ans = []
    tem = 1
    for i in range(len(arr)):
        tem *= arr[i]
        ans.append(tem)
 
    return ans
 
def suf(arr):
    ans = []
    tem = 1
    for i in range(len(arr)-1,-1,-1):
        tem *= arr[i]
        ans.append(tem)
 
    return ans
        
 
from bisect import bisect_left        
for _ in range(ii()):
    n = ii()
    arr = sorted(list(set(lii())))
     
    m =  max(arr)
    ans = 0
    for i in range(len(arr)):
        a = bisect_left(arr,arr[i]+n)
        d = a - i
        ans = max(ans,d)
    
 
    
    print(ans)