#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of each type initially.
def func():
    for ii in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        r = a[0]
        
        rem = 0
        
        y = 0
        
        for i in range(0, n - 1):
            if (i + 1) * (a[i + 1] - a[i]) > k:
                r = a[i] + k // (i + 1)
                rem = k % (i + 1)
                y = n - 1 - i
                k = 0
                break
            else:
                k -= (i + 1) * (a[i + 1] - a[i])
                r = a[i + 1]
        
        if k != 0:
            r = a[n - 1] + k // n
            print((r - 1) * n + 1 + k % n)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: Output State: After the loop executes all the iterations, `ii` will be equal to the total number of test cases (let's call it `total_test_cases`), `a` will be a sorted list of integers as it was initially, `i` will be `n-1`, `n` will be 0, `k` will be 0, `r` will be the last element of the original list `a` plus `k` divided by `n` (which is 0 since `n` is 0), `rem` will be 0, and `y` will be 1.
    #
    #This means that after processing all test cases, the loop will have iterated through each test case exactly once, and for each test case, it will have adjusted the value of `r` based on the conditions provided. Finally, when there are no more test cases (`ii` equals `total_test_cases`), the loop ends, and the output will be calculated using the final value of `r`, which is essentially the last element of the last processed list `a`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \) and \( k \), and a list \( a \) of \( n \) integers. For each test case, it sorts the list \( a \) and calculates a new value \( r \) based on the elements of \( a \) and the value of \( k \). It then adjusts \( r \) according to certain conditions involving \( k \) and the differences between consecutive elements in \( a \). After processing all test cases, it prints a final value derived from the last calculated \( r \) and the remaining values of \( k \) and other variables.

