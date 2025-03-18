#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50,000, k is an integer such that 1 ≤ k ≤ ⌊n/2⌋, and a is a list of 2n integers where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 50,000.
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
        
    #State: After all iterations, for each test case, exactly `k` values have been printed, and no further values are printed for that test case. The variables `ldb`, `rdb`, `sng`, and `sz` are reset for each new test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n`, an integer `k`, and a list `a` of 2n integers where each integer from 1 to n appears exactly twice. It then prints `k` integers from the list, ensuring that the printed integers are chosen such that if an integer appears twice in the list, it is printed twice if possible, and otherwise, it is printed once. The function ensures that exactly `k` integers are printed for each test case.

