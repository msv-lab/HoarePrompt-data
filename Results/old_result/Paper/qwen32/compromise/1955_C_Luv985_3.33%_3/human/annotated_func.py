#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^15. a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n across all test cases does not exceed 2 · 10^5.
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
        
    #State: n is 5, k is 0, l is 2, r is 3, ans is 3, T is 0, a is [0, 0, 5, 6, 0].
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers `a` and an integer `k`. For each test case, it calculates the maximum number of pairs of elements in `a` that can be reduced to zero by subtracting up to `k` from their sum, and prints the result.

