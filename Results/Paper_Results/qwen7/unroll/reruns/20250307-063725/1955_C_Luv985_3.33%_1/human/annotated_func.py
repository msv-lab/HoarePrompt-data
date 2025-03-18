#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^15; a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9, and the sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state will be the sum of the number of elements in the list `a` that become zero after performing the specified operations for each pair of indices `(l, r)` as described in the loop body, for all iterations provided by the input integer `T`.
    #
    #In each iteration, the code processes a new pair of integers `n` and `k`, followed by a list `a` of `n` integers. It then iteratively reduces the values at the leftmost (`l`) and rightmost (`r`) indices of the list `a` using the value of `k`. If the minimum of `a[l]` and `a[r]` is less than or equal to half of `k`, both `a[l]` and `a[r]` are reduced by this minimum value, and `k` is decreased accordingly. If one of the elements becomes zero, it contributes to the count `ans`. If `k` is not completely used up, the remaining part of `k` is applied to the larger element, and if it results in the larger element becoming zero, it also contributes to `ans`. If `l` equals `r`, the remaining value of `k` is checked against the single element `a[l]` to see if it can be reduced to zero, contributing to `ans` if possible.
    #
    #The final output is the total count of such reductions across all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( T \), followed by pairs of integers \( n \) and \( k \), and a list \( a \) of \( n \) positive integers. For each test case, it iterates through the list \( a \) and reduces the values at the leftmost and rightmost indices using the value of \( k \). It counts the number of elements in the list \( a \) that become zero after these reductions. Finally, it outputs the total count of such reductions across all test cases.

