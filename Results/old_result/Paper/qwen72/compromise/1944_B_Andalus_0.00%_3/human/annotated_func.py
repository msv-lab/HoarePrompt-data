#State of the program right berfore the function call: The function `func` is expected to take two parameters: an integer `n` and an integer `k`, where `2 <= n <= 5 * 10^4` and `1 <= k <= floor(n / 2)`. Additionally, it should take a list `a` of length `2n` containing integers from `1` to `n`, each appearing exactly twice.
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
        
    #State: After all iterations of the loop, `T` is 0, `sz` is the smallest even number greater than or equal to `k` for each iteration, and the elements from `ldb` and `rdb` that are printed are the first `min(k // 2, len(ldb))` and `min(k // 2, len(rdb))` elements respectively, each printed twice. Elements from `sng` are printed up to `k` times, ensuring `sz` reaches `k` if possible. The lists `lft`, `rgt`, `ldb`, `rdb`, and `sng` are processed for each iteration but are reset for the next iteration.
#Overall this is what the function does:The function `func` reads an integer `T` from input, representing the number of test cases. For each test case, it reads two integers `n` and `k`, and a list `a` of length `2n` containing integers from `1` to `n`, each appearing exactly twice. It then splits `a` into two halves, `lft` and `rgt`, sorts them, and identifies duplicate and single elements in `lft` and duplicate elements in `rgt`. The function prints pairs of duplicate elements from `lft` and `rgt` and single elements from `lft` to reach a total of `k` elements, ensuring that the printed elements are as specified in the code. The function does not return any value. After processing all test cases, `T` is 0, and the lists `lft`, `rgt`, `ldb`, `rdb`, and `sng` are reset for each test case.

