import sys
testing = len(sys.argv) == 4 and sys.argv[3] == "myTest"
if testing:
    cmd = sys.stdout
    from time import time
    start_time = int(round(time() * 1000)) 
    input = open(sys.argv[1], 'r').readline
    sys.stdout = open(sys.argv[2], 'w')
else:
    input = sys.stdin.readline

# from math import ceil
# from collections import defaultdict as dd
# from heapq import *
############ ---- I/O Functions ---- ############
def intin():
    return(int(input()))
def intlin():
    return(list(map(int,input().split())))
def chrin():
    s = input()
    return(list(s[:len(s) - 1]))
def strin():
    s = input()
    return s[:len(s) - 1]
def intlout(l):
    print(" ".join(map(str, l)))
    
def getSum( BITree, index):
    sum = 0 # Initialize result 
     
    # Traverse ancestors of BITree[index] 
    while (index > 0): 
 
        # Add current element of BITree to sum 
        sum += BITree[index] 
 
        # Move index to parent node in getSum View 
        index -= index & (-index) 
 
    return sum
 
# Updates a node in Binary Index Tree (BITree) 
# at given index in BITree. The given value
# 'val' is added to BITree[i] and all of its
# ancestors in tree. 
def updateBIT(BITree, n, index, val):
 
    # Traverse all ancestors and add 'val' 
    while (index <= n): 
 
        # Add 'val' to current node of BI Tree 
        BITree[index] += val 
 
        # Update index to that of parent
        # in update View 
        index += index & (-index) 
 
# Returns count of inversions of size three 
def getInvCount(arr, n):
 
    invcount = 0 # Initialize result 
 
    # Find maximum element in arrays 
    maxElement = max(arr)
 
    # Create a BIT with size equal to 
    # maxElement+1 (Extra one is used 
    # so that elements can be directly 
    # be used as index)
    BIT = [0] * (maxElement + 1) 
    for i in range(1, maxElement + 1): 
        BIT[i] = 0
    for i in range(n - 1, -1, -1):
 
        invcount += getSum(BIT, arr[i] - 1) 
        updateBIT(BIT, maxElement, arr[i], 1) 
    return invcount 

def main():
    n,k = intlin()
    if n == k:
        return range(1,k+1)
    if n == k+1:
        return range(1,k+1-2) + [k,k-1]
    a = range(1,k+1) + range(k-1,2*k-n-1,-1)
    maxInv = getInvCount(a,n)
    for i in xrange(2*k-n, k):
        a[k-1] = i
        a[k-2] = k
        a[k] = k
        curInv = getInvCount(a,n)
        if curInv <= maxInv:
            ans = range(1,k+1)
            ans[k-1] = i
            ans[i-1] = k
            return ans


if __name__ == "__main__":
    for _ in xrange(intin()):
        print(main())
        # print("YES" if main() else "NO")
    # main()

    if testing:
        sys.stdout = cmd
        print(int(round(time() * 1000))  - start_time)