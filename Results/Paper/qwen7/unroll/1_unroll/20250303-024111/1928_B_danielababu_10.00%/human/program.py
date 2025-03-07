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
        
 
        
for _ in range(ii()):
    n = ii()
    arr = lii()
     
    m =  max(arr)
    new= []
    for i in range(n):
        new.append(m - arr[i]+1)
    
    new.sort()
    ans = set()
    for i in new:
        if i <= n and i >0:
            ans.add(i)
    
    print(len(ans))