#State of the program right berfore the function call: a is a list of integers of length 2n where each integer from 1 to n appears exactly twice, and k is an integer such that 1 \leq k \leq \lfloor \frac{n}{2} \rfloor.
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
        
    #State: The loop has completed all `T` iterations. `sz` is the total number of elements printed from `ldb` and `sng` in the first half of the loop and from `rdb` and `sng` in the second half of the loop, which is `min(k, 2 * len(ldb)) + min(len(sng), k - min(k, 2 * len(ldb))) + min(k, 2 * len(rdb)) + min(len(sng), k - min(k, 2 * len(rdb)))`. `ldb` and `rdb` contain all elements that appeared consecutively in `lft` and `rgt`, respectively. `sng` contains all elements from `lft` that are not equal to their previous or next elements, and the same for `rgt`. The elements in `sng` that were printed are no longer in `sng`. The elements in `ldb` and `rdb` that were printed are no longer in `ldb` and `rdb`.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it takes a list `a` of integers of length 2n, where each integer from 1 to n appears exactly twice, and an integer `k` such that 1 ≤ k ≤ ⌊n/2⌋. It then prints up to `k` pairs of integers from the first half of the list and up to `k` pairs of integers from the second half of the list. The pairs are formed by consecutive duplicates in the sorted halves of the list, and any remaining single elements from the sorted halves. The function does not return any value. After the function concludes, the input list `a` and the integer `k` are unchanged, but the internal state variables `ldb`, `rdb`, and `sng` used for processing are reset for each test case.

