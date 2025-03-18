#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n, k, and x are integers for each test case such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ k, x ≤ n, and a is a list of n integers where 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates `t` times, and for each iteration, it processes the input values `n`, `k`, and `x`, and the list `a`. After sorting `a` in descending order, it calculates two sums, `ans1` and `ans2`, where `ans1` is modified by subtracting twice the value of the first `x` elements and then adding and subtracting elements based on `k` and `x`. The final value of `ans2` for each test case is printed. The variables `t`, `n`, `k`, `x`, and `a` are reset for each test case, and the loop continues until all `t` test cases are processed.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves an integer `n`, integers `k` and `x`, and a list of `n` integers `a`. The function sorts the list `a` in descending order and calculates two sums, `ans1` and `ans2`. `ans1` is initially the sum of all elements in `a`, then it subtracts twice the value of the first `x` elements. It further modifies `ans1` by adding the first `k` elements and subtracting twice the value of elements at positions `i + x` (if they exist). The maximum value between `ans1` and `ans2` is stored in `ans2`. The function prints the final value of `ans2` for each test case. The variables `t`, `n`, `k`, `x`, and `a` are reset for each test case, and the loop continues until all `t` test cases are processed.

