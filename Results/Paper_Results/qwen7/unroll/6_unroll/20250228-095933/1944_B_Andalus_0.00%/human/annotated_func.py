#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The array a is a list of 2n integers where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: The output will consist of pairs of elements from the left sorted part of the list followed by single elements, ensuring no more than `k` elements are printed in each line. If there are repeated elements in the left sorted part, the first occurrence of the repeated element will be printed once, and subsequent occurrences will be printed as pairs until `k` elements are printed or there are no more elements to print. The same process is applied to the right sorted part, but only single elements are printed from it. Elements are taken from the sorted parts in order until `k` elements are printed per line or all elements are processed.
#Overall this is what the function does:The function processes a list of 2n integers where each integer from 1 to n appears exactly twice. For each test case, it outputs pairs of elements from the left sorted part of the list followed by single elements from both the left and right sorted parts, ensuring no more than `k` elements are printed in each line. Repeated elements in the left sorted part are handled such that the first occurrence is printed once, and subsequent occurrences are printed as pairs until `k` elements are printed or there are no more elements to print. The same process is applied to the right sorted part, but only single elements are printed from it. Elements are taken from the sorted parts in order until `k` elements are printed per line or all elements are processed.

