#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^15. a is a list of n integers such that 1 <= a_i <= 10^9. The sum of n across all test cases does not exceed 2 * 10^5.
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
                if a[l] - t - k // 2 == 0:
                    ans += 1
                break
        
        if l == r:
            ans += k >= a[l]
        
        print(ans)
        
    #State: T: 0, n: last_test_case_n, k: last_test_case_k, a: last_test_case_a, l: last_l, r: last_r, ans: last_ans.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, a long integer `k`, and a list `a` of `n` integers. For each test case, it calculates and prints the maximum number of pairs of elements from the list `a` that can be reduced to zero by subtracting equal values from both elements, with the total subtraction not exceeding `k`. If there is a single element left, it checks if `k` is sufficient to reduce it to zero.

