#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n and k are integers such that 1 <= n <= 2 \cdot 10^5 and 1 <= k <= 10^{15}, and a is a list of n integers such that 1 <= a_i <= 10^9.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` and `k` are integers such that 1 <= n <= 2 \cdot 10^5 and 1 <= k <= 10^{15}, `a` is a list of `n` integers such that 1 <= a_i <= 10^9, `T` is 0, `l` and `r` are integers such that 0 <= l <= n and 0 <= r < n, `ans` is an integer such that 0 <= ans <= n. If `l` is equal to `r` and `k` is greater than or equal to `a[l]`, `ans` is incremented by 1; otherwise, `ans` remains unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads two integers `n` and `k`, and a list `a` of `n` integers. It then calculates the maximum number of pairs of elements from `a` that can be reduced to zero by subtracting the minimum of the pair from both elements, while also decrementing `k` by twice the minimum value. If `k` is still positive and there is a single element left, it checks if `k` is greater than or equal to this element and increments the count if true. The function prints the count of such pairs and single elements for each test case. After processing all test cases, `T` is 0, and the function does not return any value.

