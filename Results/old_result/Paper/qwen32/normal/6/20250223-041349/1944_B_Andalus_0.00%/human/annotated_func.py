#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n and k are integers such that 2 <= n <= 5 * 10^4 and 1 <= k <= floor(n/2). a is a list of 2n integers where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 5 * 10^4.
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
        
    #State: The loop will have printed the first `k` elements of the list `sng` (or the first `floor(k/2)*2` elements if `k` is odd) for both `lft` and `rgt`, and `sz` will be equal to `k` (or the largest even number less than or equal to `k` if `k` is odd) for both iterations of `lft` and `rgt`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers `n` and `k`, and a list `a` of `2n` integers. It then prints out `k` integers from the list, prioritizing pairs of identical numbers, and if necessary, single occurrences, from both the first half and the second half of the list separately.

