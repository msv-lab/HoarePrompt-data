#State of the program right berfore the function call: t is an integer where 1 <= t <= 5000, n and k are integers for each test case such that 2 <= n <= 50000 and 1 <= k <= floor(n/2), and a is a list of 2n integers where 1 <= a_i <= n, with each integer from 1 to n appearing exactly twice.
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
        
    #State: The loop processes t test cases, where for each test case, it prints pairs of integers from the list `a` that appear twice in the first half of the list until k pairs are printed. If fewer than k pairs are found, it prints additional integers from the first half of the list that appear only once until 2k integers are printed. It then prints the remaining integers from the first half of the list that were not printed in the previous steps. Finally, it prints pairs of integers from the second half of the list that appear twice until the number of printed integers from the first half matches the number of printed integers from the second half.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads an integer `n` and an integer `k`, and a list `a` of 2n integers where each integer from 1 to n appears exactly twice. It prints pairs of integers from the first half of `a` that appear twice until `k` pairs are printed. If fewer than `k` pairs are found, it prints additional integers from the first half of `a` that appear only once until a total of `2k` integers are printed. It then prints the remaining integers from the first half of `a` that were not printed in the previous steps. Finally, it prints pairs of integers from the second half of `a` that appear twice until the number of printed integers from the first half matches the number of printed integers from the second half. The function does not return any value.

