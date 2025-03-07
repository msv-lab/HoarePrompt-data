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
                    ur += 2
                if ul == ur:
                    break
        
        print()
        
    #State: t remains the same, n remains the same, a remains the same, l remains the same, r remains the same, ul is either k * 2 or the number of pairs found, ur equals ul, re is the number of unique elements with count 1 found up to k, res contains the unique elements printed, k remains the same.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n`, an integer `k`, and a list `a` of 2n integers. For each test case, it prints pairs of integers from the list `a` based on specific conditions related to the frequency of each integer in the list. The function ensures that it prints `k` pairs of integers that appear exactly twice in the list, and if necessary, it prints additional unique integers that appear only once to reach the required count of `k` pairs. The function maintains the input values `t`, `n`, and `a` unchanged and outputs the specified integers for each test case.

