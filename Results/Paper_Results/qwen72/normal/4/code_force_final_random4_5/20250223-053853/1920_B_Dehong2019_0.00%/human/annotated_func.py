#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, k, and x are integers for each test case such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ x, k ≤ n, and a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop executes `t` times, and for each iteration, it prints the maximum possible value of `ans1` after performing the specified operations on the array `a`. The variables `t`, `n`, `k`, `x`, and `a` are not retained between iterations, so they are reset for each new test case. The final state of these variables is undefined after the loop completes, but the output for each test case is the maximum value of `ans1` as calculated during that iteration.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `k`, and `x`, and a list of integers `a` of length `n`. For each test case, it calculates and prints the maximum possible value of a modified sum of the elements in `a`. The modifications involve subtracting twice the value of the first `x` elements and then adding the value of the first `k` elements while subtracting twice the value of the elements at positions `x + 1` to `k + x` (if they exist). The variables `t`, `n`, `k`, `x`, and `a` are reset for each test case, and their final state is undefined after the function completes.

