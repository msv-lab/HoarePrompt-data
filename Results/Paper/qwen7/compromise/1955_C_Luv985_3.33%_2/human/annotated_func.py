#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^{15}; a is a list of n integers such that 1 ≤ a_i ≤ 10^9. Additionally, the sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: All instances of `T` will be 0 since the loop continues as long as `T` is truthy (non-zero) and is decremented by 1 each iteration until it reaches 0. The variable `n` will hold the value it had after the last iteration of the loop, and `k` will also reflect its final value post-loop, which is guaranteed to be 0 or negative because the loop reduces `k` until it can no longer be reduced. The list `a` will contain the remaining values after all possible reductions have been applied according to the rules described in the loop body. Variable `l` will be equal to `r`, and `r` will be equal to `n - 1`. The variable `ans` will be the total count of elements in `a` that became zero during the loop iterations plus any additional count if `k` was still non-negative and greater than or equal to `a[l]` at the end. The variable `mi` will hold the minimum value between `a[l]` and `a[r]` in the last operation, and `t` will be `k % 2` if the loop broke due to `mi * 2 > k`.
    #
    #Since the loop runs until `T` becomes 0, the final state of the program will have `T` as 0, with all other variables reflecting their final states after the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer \( T \) (number of test cases), an integer \( n \) (length of the list), an integer \( k \) (initial value), and a list of \( n \) integers \( a \). For each test case, the function repeatedly reduces pairs of elements in the list \( a \) by their minimum value, up to \( k \) times, until no further reductions are possible or \( k \) becomes zero. It counts the number of elements in the list that become zero after these operations and prints this count for each test case.

