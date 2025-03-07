#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, k ≤ n. Additionally, there is a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 1000. The sum of n across all test cases does not exceed 2 ⋅ 10^5.
def func():
    """
    Created on Fri Sep  6 21:42:15 2024
     
    @author: dehon
    """
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        
        a = sorted(list(map(int, input().split())), reverse=True)
        
        ans1 = sum(a)
        
        for i in range(x):
            ans1 -= a[i] * 2
        
        ans2 = ans1
        
        for i in range(k):
            ans1 += a[i]
            if i + x < n:
                ans1 -= a[i + x] * 2
            ans = max(ans1, ans2)
        
        print(ans)
        
    #State: Output State: t is the number of test cases, for each test case, n, k, and x are positive integers with the given constraints, and a is a list of n integers sorted in non-increasing order. After executing the loop, ans is the maximum value between ans1 and ans2, where ans1 is updated based on the first x elements and the next k elements of the list a.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads positive integers `n`, `k`, and `x`, and a list of `n` integers `a`. It sorts the list `a` in non-increasing order. Then, it calculates two values, `ans1` and `ans2`, by adjusting the sum of the list based on the first `x` elements and the next `k` elements. Finally, it prints the maximum of these two values for each test case.

