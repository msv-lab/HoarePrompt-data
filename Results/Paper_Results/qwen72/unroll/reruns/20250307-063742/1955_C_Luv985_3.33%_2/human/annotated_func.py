#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, n and k are integers where 1 <= n <= 2 * 10^5 and 1 <= k <= 10^15, and a is a list of n integers where 1 <= a_i <= 10^9.
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
        
    #State: T is 0.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes an integer `n`, an integer `k`, and a list `a` of `n` integers. It modifies the list `a` by reducing pairs of elements from the ends of the list until the sum of the reductions equals `k` or no more pairs can be reduced. The function then prints the number of elements in the list `a` that have been reduced to zero. After processing all test cases, the function ensures that the variable `T` is 0.

