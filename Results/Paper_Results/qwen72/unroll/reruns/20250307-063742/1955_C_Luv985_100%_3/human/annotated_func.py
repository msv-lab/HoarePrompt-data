#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^15, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: The loop will have processed all `T` test cases, and for each test case, it will have printed the number of elements in the list `a` that can be reduced to zero by the operations defined in the loop. The variables `T`, `n`, `k`, and `a` will be in their final states after each test case is processed, and `t` will remain unchanged as it is not modified within the loop.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it takes an integer `n` and a long integer `k`, and a list `a` of `n` integers. It performs operations to reduce the values in `a` by pairs, and counts how many elements in `a` can be reduced to zero using the given `k`. After processing each test case, it prints the count of elements reduced to zero. The function does not return any value, but it processes all `T` test cases and prints the result for each one. The variables `T`, `n`, `k`, and `a` are reset and re-used for each test case, and the function does not modify the input parameter `t` (which is not used within the function).

