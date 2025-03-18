#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^15. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of n across all test cases does not exceed 2 * 10^5.
def func():
    """
        @Time : 2024/8/26 17:59
        @Author : Zhiliang.L
        @Email : 2410103062@mails.edu.cn
        @File : 1955-C.py
    """
    T = int(input())
    while T:
        T -= 1
        
        n, k = input().split()
        
        n = int(n)
        
        k = int(k)
        
        a = input().split()
        
        a = list(map(lambda x: int(x), a))
        
        l = 0
        
        r = n - 1
        
        ans = 0
        
        while l < r and k > 0:
            mi = min(a[l], a[r])
            if mi * 2 <= k:
                a[l] -= mi
                a[r] -= mi
                k -= mi * 2
                if a[l] == 0:
                    ans += 1
                    l += 1
                if a[r] == 0:
                    ans += 1
                    r -= 1
            else:
                t = k % 2
                if mi - t - k // 2 == 0:
                    ans += 1
                break
        
        if l == r:
            ans += k >= a[l]
        
        print(ans)
        
    #State: - The loop will continue to execute until `T` becomes 0.
    #   - After all iterations are complete, `T` will be 0.
    #   - The variables `n`, `k`, `a`, `l`, `r`, and `ans` will reflect the state after processing the last test case.
    #   - The final value of `ans` for each test case is printed, but the overall final state of the loop will be characterized by `T` being 0.
    #
    #Given the nature of the problem and the provided output states after the first 3 iterations, the final output state after all iterations will be:
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `k`, and a list `a` of `n` integers. For each test case, it calculates and prints the maximum number of pairs of elements in the list that can be reduced to zero by subtracting a value such that the sum of the values subtracted from each pair does not exceed `k`.

