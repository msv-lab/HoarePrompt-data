#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^{15}; a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9, where a_i represents the durability of the i-th ship. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The value of `ans` will be the total number of elements in the list `a` that become zero after performing the specified operations for each pair of indices `(l, r)` as described in the loop.
    #
    #To understand this output state, let's break down the process:
    #
    #1. For each test case (`T`), we read two integers `n` and `k`, followed by a list `a` of `n` integers.
    #2. We initialize two pointers `l` and `r` at the start and end of the list `a`, respectively.
    #3. We also initialize `ans` to count how many elements in `a` become zero.
    #4. In the inner while loop, we perform operations on the elements at positions `l` and `r` until either `l` equals `r` or `k` becomes zero.
    #   - If the minimum of `a[l]` and `a[r]` times 2 is less than or equal to `k`, we subtract this minimum value from both `a[l]` and `a[r]`, reduce `k` accordingly, and increment `ans` if either `a[l]` or `a[r]` becomes zero.
    #   - Otherwise, we adjust `k` using modulo and integer division, and check if `a[l]` can be reduced to zero with the remaining `k`. If so, we increment `ans`.
    #5. If `l` equals `r` and there's still some `k` left, we check if `a[l]` can be reduced to zero with the remaining `k`.
    #6. Finally, we print the value of `ans`.
    #
    #The output state is the final value of `ans`, which represents the total number of elements in `a` that have been reduced to zero after all possible operations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of ship durabilities and two integers. For each test case, it determines the number of ships whose durability can be reduced to zero by repeatedly selecting pairs of ships and reducing their durability based on a given limit. The function prints the total count of ships whose durability is reduced to zero for all test cases.

