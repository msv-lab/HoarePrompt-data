#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of type i initially.
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
            print((r - 1) * n + 1)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: After all iterations of the loop have finished, the variable `ii` will be equal to the total number of test cases, `n` will be less than or equal to 2 * 10^5, `k` will be 0, `r` will be the last element of the list `a` (`a[n-1]`), `rem` will be 0, `y` will be 0, and `i` will be `n - 1`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`, and a list `a` of `n` integers. For each test case, it sorts the list `a` and then iterates through it to find the maximum possible value `r` that can be achieved by distributing `k` among the elements of `a`. If `k` cannot be fully distributed, it calculates the remaining value `rem` and the count `y` of elements that can still receive additional values. Finally, it prints the result based on the distribution of `k` and the values of `r`, `rem`, and `y`.

