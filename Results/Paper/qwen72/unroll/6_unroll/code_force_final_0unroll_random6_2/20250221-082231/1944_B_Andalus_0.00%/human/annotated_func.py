#State of the program right berfore the function call: The function `func` is expected to take two parameters, `a` and `k`, where `a` is a list of integers of length 2n, containing each integer from 1 to n exactly twice, and `k` is an integer such that 1 ≤ k ≤ ⌊n/2⌋. The function should be called within a loop that processes multiple test cases, each defined by a pair of integers `n` and `k`, and the list `a`.
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
        
    #State: The loop processes `T` test cases. For each test case, after the loop executes, the variables `n`, `k`, `lst`, `lft`, `rgt`, `ldb`, `rdb`, and `sng` are updated based on the input for the next test case. The `sz` variable is reset to 0 at the beginning of each test case. The loop prints pairs of elements from `ldb` and `rdb` and single elements from `sng` up to `k` elements for each of the left and right halves of the list. After all iterations, the loop completes and the program ends.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by a pair of integers `n` and `k`, and a list `a` of integers of length 2n, where each integer from 1 to n appears exactly twice. For each test case, the function splits the list `a` into two halves, sorts them, and then prints pairs of duplicate elements from each half and single elements from the first half, up to `k` elements in total for each half. After processing all test cases, the function completes and the program ends.

