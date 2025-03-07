#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The list a is a list of 2n integers where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: The output consists of multiple lines, each representing the results of one test case. For each test case, it first prints pairs of numbers that appear exactly twice in the list `a` and have their counts in the list `l` equal to 2, up to `k*2` such pairs. After printing these pairs, it prints the remaining numbers from the list `res`, which are the numbers that appeared once in the first half of the list `a` and are needed to reach `2*k - ul` unique numbers. Finally, it prints any pairs of numbers from the second half of the list `a` that have their counts in the list `r` equal to 2, until `ul` equals `ur`. Each line ends with a space-separated list of numbers printed during the test case.
#Overall this is what the function does:The function processes a list of 2n integers where each integer from 1 to n appears exactly twice, along with two integers n and k. It prints pairs of numbers that appear exactly twice in the list and have their counts in the list `l` equal to 2, up to `k*2` such pairs. After printing these pairs, it prints the remaining numbers from the list `res`, which are the numbers that appeared once in the first half of the list `a` and are needed to reach `2*k - ul` unique numbers. Finally, it prints any pairs of numbers from the second half of the list `a` that have their counts in the list `r` equal to 2, until `ul` equals `ur`. Each line ends with a space-separated list of numbers printed during the test case.

