#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50,000, and k is an integer such that 1 <= k <= floor(n/2). a is a list of 2n integers where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 50,000.
def func():
    for _ in range(int(input())):
        n, k = [int(i) for i in input().split()]
        
        a = [int(i) for i in input().split()]
        
        l = [0] * n
        
        r = [0] * n
        
        re = ul = ur = 0
        
        res = []
        
        for i in range(n):
            l[a[i] - 1] += 1
        
        for i in range(n, 2 * n):
            r[a[i] - 1] += 1
        
        for i in range(n):
            if l[a[i] - 1] == 2:
                print(a[i], a[i], end=' ')
                l[a[i] - 1] = 0
                ul += 2
            if ul == k * 2:
                break
        
        k = 2 * k - ul
        
        if k:
            for i in range(n):
                if l[a[i] - 1] == 1:
                    print(a[i], end=' ')
                    re += 1
                    res.append(a[i])
                if re == k:
                    break
        
        print()
        
        for i in res:
            print(i, end=' ')
        
        if ul != ur:
            for i in range(n, 2 * n):
                if r[a[i] - 1] == 2:
                    print(a[i], a[i], end=' ')
                    r[a[i] - 1] = 0
                    ur += 2
                if ul == ur:
                    break
        
        print()
        
    #State: All integers from 1 to n are printed exactly twice, `ul` and `ur` are equal to `2 * k`, `res` is empty, `re` is 0, `l` and `r` are arrays of zeros, `a` remains unchanged, `k` is 0.
#Overall this is what the function does:For each test case, the function processes a list of 2n integers where each integer from 1 to n appears exactly twice. It prints integers from the list according to specific rules related to the count `k`. The function ensures that each integer from 1 to n is printed exactly twice across all outputs for each test case.

