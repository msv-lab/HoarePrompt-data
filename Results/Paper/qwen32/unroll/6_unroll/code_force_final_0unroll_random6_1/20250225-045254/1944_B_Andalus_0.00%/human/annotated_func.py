#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 5 * 10^4, and k is an integer such that 1 <= k <= floor(n/2). The array a is a list of 2n integers where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 5 * 10^4.
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
        
    #State: The output state is a series of printed elements for each test case, where for each test case, up to `k` elements are printed from the duplicates in `lft` and `rgt`, and if necessary, from the singletons in `lft`. Each test case's output is followed by a newline.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n`, an integer `k`, and an array `a` of 2n integers where each integer from 1 to n appears exactly twice. It then prints up to `k` elements from the duplicates in the first half and second half of the array, and if necessary, from the singletons in the first half. The output for each test case is followed by a newline.

