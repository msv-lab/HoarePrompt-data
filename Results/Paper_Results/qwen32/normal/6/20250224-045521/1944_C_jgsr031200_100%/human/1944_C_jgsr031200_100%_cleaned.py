"""
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
 
 
# Read tree as graph
def build_tree(n,arr):
    tree = {(i+1):[] for i in range(n)}
    for (i,j) in arr:
        tree[i].append(j)
        tree[j].append(i)
    return tree
 
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
 
# Kadanes
def kadane(arr):
    n = len(arr)
    pre = 0
    maxi = 0
    for i in range(n):
        pre = max(pre+arr[i],arr[i])
        maxi = max(maxi,pre)
    #print('max',maxi)
    return maxi
 
# dfs
def dfs(root,par,tree):
    c = 1
    for v in tree[root]:
        if v!=par:
            c+=dfs(v,root,tree,x)
    return c
"""
big = 1000000007

def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        if freq[i] == 1:
            cou += 1
        if cou == 2 or freq[i] == 0:
            print(i)
            break
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    func_1(arr)