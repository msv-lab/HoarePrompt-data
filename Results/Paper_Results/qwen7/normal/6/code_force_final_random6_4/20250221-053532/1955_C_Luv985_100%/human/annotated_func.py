#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^15. a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9, where a_i represents the durability of the i-th ship. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The loop has completed all its iterations, and the following conditions hold:
    #
    #- `T` is `False`, indicating that the while loop condition `T` is no longer satisfied.
    #- `n` is an integer value that was read from the input during the last iteration of the loop.
    #- `k` is `0`, as it is decremented to `0` in each iteration where `l < r` and `k > 0` are true, and remains `0` afterward.
    #- `a` is a list of integers that has been modified throughout the iterations. After all iterations, `a` contains only zeros and possibly some positive integers, depending on the input values.
    #- `l` and `r` are such that they either point to the last remaining non-zero element in `a` or are out of bounds if all elements in `a` have become zero.
    #- `ans` is the total count of zeros in the list `a` after all iterations. It is incremented by `1` for each zero encountered in `a[l]` or `a[r]` when `l` equals `r`, and also by `1` if `k` is greater than or equal to `a[l]` when `l` equals `r`.
    #
    #In summary, after all iterations, the list `a` will contain only zeros and possibly some positive integers, `l` and `r` will point to the last remaining non-zero elements or be out of bounds, and `ans` will be the total count of zeros in `a`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes the number of ships \( n \), the durability reduction limit \( k \), and a list of ship durabilities \( a \). It then iteratively reduces the durability of the ships from both ends towards the center until no further reductions can be made or \( k \) becomes zero. The function counts the total number of ships whose durability is reduced to zero and prints this count for each test case.

