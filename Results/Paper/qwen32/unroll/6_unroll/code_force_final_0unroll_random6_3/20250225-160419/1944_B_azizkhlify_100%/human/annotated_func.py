#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50,000, and k is an integer such that 1 ≤ k ≤ ⌊n/2⌋. a is a list of 2n integers where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 50,000.
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
        
    #State: The variables `l`, `r`, `re`, `ul`, `ur`, and `res` will be updated based on the processing of the list `a`. The list `a` will remain unchanged. The printed output will consist of integers from the list `a` as described above.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `k`, and a list `a` of 2n integers where each integer from 1 to n appears exactly twice. For each test case, it prints a sequence of integers from `a` based on specific rules: first, it prints `k` pairs of integers that appear twice in the first half of `a`; then, if needed, it prints additional integers from the first half of `a` that appear only once, up to a total of `k` such integers; finally, it prints the remaining integers from the second half of `a` that appear twice, ensuring the total number of printed integers matches the requirements.

