#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, k, and x are integers for each test case such that 1 ≤ n ≤ 2·10^5, 1 ≤ k, x ≤ n, and a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2·10^5.
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
            ans2 = max(ans1, ans2)
        
        print(ans2)
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n`, `k`, and `x` from input, sorts the list `a` in descending order, and calculates the maximum possible value of `ans2` after applying the specified operations. The final value of `ans2` is printed for each test case. The state of `t`, `n`, `k`, `x`, and `a` is reset for each iteration, and the variables `ans1` and `ans2` are recalculated for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads integers `n`, `k`, and `x`, and a list of integers `a` of length `n`. It then sorts the list `a` in descending order and calculates the maximum possible value of a modified sum of the elements in `a` based on the values of `k` and `x`. The final value of this modified sum, `ans2`, is printed for each test case. The state of `t`, `n`, `k`, `x`, and `a` is reset for each iteration, and the variables `ans1` and `ans2` are recalculated for each test case.

