#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50,000, and k is an integer such that 1 ≤ k ≤ ⌊n/2⌋. The array a is a list of 2n integers where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 50,000.
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
        
    #State: The output state consists of T test cases, each producing two lines of output. For each test case, the first line contains up to k integers selected from the left half (lft) and the right half (rgt) of the input list `lst`, prioritizing pairs of identical integers from each half. If there are not enough pairs to reach k integers, single integers from the left half are added until k integers are reached. The second line follows the same logic but exclusively uses integers from the right half (rgt). The state of variables `T`, `t`, `n`, `k`, and `lst` remains unchanged after each iteration of the loop, except for the temporary variables `lft`, `rgt`, `ldb`, `rdb`, `sng`, and `sz` which are recalculated for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`, an integer `k`, and an array `a` of 2n integers where each integer from 1 to n appears exactly twice. For each test case, it outputs two lines. The first line contains up to `k` integers selected from the left half of the array, prioritizing pairs of identical integers. If there are not enough pairs, it includes single integers until `k` integers are reached. The second line follows the same logic but uses only integers from the right half of the array.

