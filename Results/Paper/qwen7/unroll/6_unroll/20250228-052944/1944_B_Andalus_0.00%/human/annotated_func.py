#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The list a is a list of 2n integers where each integer from 1 to n appears exactly twice.
def func():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        
        lst = list(map(int, input().split()))
        
        lft = lst[:n]
        
        rgt = lst[n:]
        
        ldb = []
        
        rdb = []
        
        sng = []
        
        lft.sort()
        
        rgt.sort()
        
        for i in range(1, n):
            if lft[i] == lft[i - 1]:
                ldb.append(lft[i])
            elif i < n - 1 and lft[i] != lft[i + 1]:
                sng.append(lft[i])
        
        for i in range(1, n):
            if rgt[i] == rgt[i - 1]:
                rdb.append(rgt[i])
        
        sz = 0
        
        for elem in ldb:
            if sz >= k:
                break
            if k - sz >= 2:
                print(elem, elem, end=' ')
                sz += 2
        
        for elem in sng:
            if sz >= k:
                break
            print(elem, end=' ')
            sz += 1
        
        print()
        
        sz = 0
        
        for elem in rdb:
            if sz >= k:
                break
            if k - sz >= 2:
                print(elem, elem, end=' ')
                sz += 2
        
        for elem in sng:
            if sz >= k:
                break
            print(elem, end=' ')
            sz += 1
        
    #State: Output State: The output will consist of pairs of elements from the sorted left part of the list (lft) and single elements from both the left and right parts of the list (lft and rgt), printed in groups of up to `k` elements. If there are enough repeated elements in the left part, they will be printed in pairs first, followed by single elements. The same process is repeated for the right part of the list. If the total number of elements to be printed exceeds `k`, only up to `k` elements will be printed.
#Overall this is what the function does:The function processes a list of 2n integers (where each integer from 1 to n appears exactly twice) along with two integers n and k. It outputs pairs of elements from the sorted left part of the list (lft) and single elements from both the left and right parts of the list (lft and rgt), printed in groups of up to k elements. If there are enough repeated elements in the left part, they will be printed in pairs first, followed by single elements. The same process is repeated for the right part of the list. If the total number of elements to be printed exceeds k, only up to k elements will be printed.

