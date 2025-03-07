#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n and k are integers for each test case where 1 <= n <= 2 * 10^5 and 1 <= k <= 10^15, and a is a list of n integers where 1 <= a_i <= 10^9.
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
        
    #State: `T` is 0, `n` is an integer greater than 1, `k` is 0 or a positive integer, `a` is a list of integers where elements between `l` and `r` (inclusive) are non-zero, while elements before `l` and after `r` are zero, `l` is an integer between 0 and `n - 1`, `r` is an integer between 0 and `n - 1`, `ans` is an integer between 0 and `n - 1`. If `l` is equal to `r`, `ans` is incremented by 1 if `k` is greater than or equal to `a[l]`, otherwise `ans` remains unchanged. If `l` is not equal to `r`, `ans` remains unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n` and `k`, and a list of `n` integers `a`. For each test case, it calculates the maximum number of elements in `a` that can be reduced to zero by repeatedly subtracting the minimum of the elements at the current left and right indices, while also decrementing `k` by twice the minimum value. The function prints the result for each test case, which is the number of elements in `a` that have been reduced to zero. After processing all test cases, the function terminates with `T` set to 0, `n` and `k` reset for each test case, `a` modified such that elements between `l` and `r` (inclusive) are non-zero, and elements before `l` and after `r` are zero, and `ans` is an integer between 0 and `n - 1`. If `l` is equal to `r` at the end of a test case, `ans` is incremented by 1 if `k` is greater than or equal to `a[l]`.

