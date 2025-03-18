#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^15; a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9, where a_i represents the durability of the i-th ship. Additionally, the sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The value of `ans` will be the sum of the number of elements in list `a` that become zero after performing the operations specified in the loop for each pair of indices `(l, r)` as many times as possible with the given `k`.
    #
    #To explain further, for each test case (determined by the value of `T`), the code processes two integers `n` and `k`, followed by a list `a` of `n` integers. It then iteratively reduces pairs of elements from the ends of the list towards the center, subtracting up to `k` from the smaller of the two elements in each pair. If both elements in a pair become zero, they are counted towards `ans`. If `k` is not sufficient to make both elements zero, the remaining `k` is applied to one element, and if that element becomes zero, it is also counted towards `ans`. The process continues until no more reductions can be made or `k` is exhausted. After processing all test cases, `ans` contains the total count of elements that became zero across all test cases.
    #
    #The final value of `ans` will depend on the specific values of `n`, `k`, and the elements in `a` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `k`, and a list `a` of `n` positive integers. For each test case, it iteratively reduces pairs of elements from the ends of the list towards the center, subtracting up to `k` from the smaller of the two elements in each pair. If both elements in a pair become zero, they are counted towards the result. If `k` is not sufficient to make both elements zero, the remaining `k` is applied to one element, and if that element becomes zero, it is also counted towards the result. The process continues until no more reductions can be made or `k` is exhausted. The function returns the total count of elements that became zero across all test cases.

