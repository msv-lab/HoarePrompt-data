#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, k ≤ n. The array a consists of n integers where 1 ≤ a_i ≤ 1000 for all elements a_i in the array. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func():
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        n, k, x = R()
        
        a = [0]
        
        for y in sorted(R()):
            a += a[-1] + y,
        
        print(max(2 * a[max(i, x) - x] - a[i] for i in range(n - k, n + 1)))
        
    #State of the program after the loop has been executed: `t` is 0, `a` is a list where each element is the cumulative sum of all elements in `R()` up to that point, `n` is the last value returned by `R()`, `k` is the last value returned by `R()`, `x` is the last value returned by `R()`, the print statement outputs the maximum value of the expression `max(2 * a[max(i, x) - x] - a[i] for i in range(n - k, n + 1))` based on the final values of `a`, `x`, `n`, and `k`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes three positive integers \( n \), \( k \), and \( x \), and an array \( a \) of \( n \) integers. It then constructs a new list \( a \) containing cumulative sums and computes the maximum value of the expression \( \max(2 \cdot a[\max(i, x) - x] - a[i]) \) for \( i \) ranging from \( n-k \) to \( n \). The function prints this maximum value for each test case. After processing all test cases, the function sets `t` to 0, and the final state of the program includes the computed results for each test case. Potential edge cases include scenarios where \( n \) is small (e.g., 1), \( k \) and \( x \) are within the bounds of \( n \), and the input values are within the specified constraints. The function does not handle invalid input directly; instead, it relies on the correctness of the input provided by the user.

