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
        
    #State: All elements of `res` have been printed. The variables `l` and `r` reflect the counts of elements in the respective halves of `a`. The variables `ul` and `ur` are equal, indicating that the number of elements appearing exactly twice in the left and right halves of `a` have been balanced. The variable `k` has been adjusted and used to print the required number of elements appearing exactly once. The loop has terminated after processing all test cases.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes an integer `n`, an integer `k`, and a list `a` of `2n` integers. It then prints pairs of integers that appear exactly twice in the list, ensuring that `k` pairs are printed from the first half of the list. If fewer than `k` pairs are found in the first half, it prints additional integers that appear exactly once until `k` pairs and `k` single integers are printed in total. Finally, it balances the output by printing pairs from the second half of the list if necessary.

