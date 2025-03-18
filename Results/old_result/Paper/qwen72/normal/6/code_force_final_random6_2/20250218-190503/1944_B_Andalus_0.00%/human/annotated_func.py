#State of the program right berfore the function call: The function `func` is expected to take two parameters, `a` and `k`, where `a` is a list of integers of length 2n, and `k` is an integer such that 1 ≤ k ≤ ⌊n/2⌋. The list `a` contains each integer from 1 to n exactly twice, and `n` is an integer such that 2 ≤ n ≤ 5 · 10^4. The function should handle multiple test cases, each defined by a pair of values `n` and `k`, and the list `a` is provided for each test case.
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
        
    #State: The loop has completed all `T` iterations. `_` is `T-1`, `n` and `k` are the values from the last test case, `lst` is the list of integers from the last test case, `lft` and `rgt` are the sorted sublists from the last test case, `ldb` and `rdb` are the lists of duplicate elements from the last test case, `sng` is the list of single elements from the last test case, and `sz` is the final value after processing all elements in `ldb` and `sng` or until `sz` reaches `k`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by a list `a` of integers of length 2n (where each integer from 1 to n appears exactly twice) and an integer `k` such that 1 ≤ k ≤ ⌊n/2⌋. For each test case, it splits the list `a` into two equal halves, sorts them, and then prints pairs of duplicate elements from the first half and single elements from the first half until it has printed `k` elements. It then repeats the process for the second half, printing pairs of duplicate elements and single elements until it has printed `k` elements. The function does not return any value; it only prints the results for each test case. After processing all test cases, the function completes and the final state includes the sorted sublists and the lists of duplicate and single elements from the last test case.

