#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 5 * 10^4, and k is an integer such that 1 <= k <= floor(n/2). a is a list of 2n integers where each integer from 1 to n occurs exactly twice. The sum of n over all test cases does not exceed 5 * 10^4.
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
        
    #State: All elements from `l` that appear exactly twice are printed twice. All remaining elements from `l` that appear once are printed until `k` elements are printed. If `ul` is not equal to `ur`, elements from `r` that appear exactly twice are printed until `ul` equals `ur`.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`, an integer `k`, and a list `a` of `2n` integers where each integer from 1 to `n` appears exactly twice. For each test case, it prints pairs of integers from the first half of `a` that appear exactly twice, then prints additional unique integers from the first half until `k` unique integers have been printed. If the count of printed pairs from the first half (`ul`) does not match the count of printed pairs from the second half (`ur`), it prints pairs of integers from the second half that appear exactly twice until the counts match.

