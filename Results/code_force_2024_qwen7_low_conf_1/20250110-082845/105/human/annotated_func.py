#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n; and an array a of length n where 1 ≤ a_i ≤ 1000 for all elements a_i in the array. The sum of n across all test cases does not exceed 2⋅10^5.
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
        
    #State of the program after the loop has been executed: `t` is 0, `n`, `k`, and `x` are the values returned by `R()` in the last iteration, `a` is a list where `a[0] = 0` and for every index `i` from 1 to `m`, `a[i] = a[i-1] + y_i`, and the maximum value of `2 * a[max(i, x) - x] - a[i]` for `i` in the range `n - k` to `n + 1` has been computed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it accepts four inputs: the number of elements `n`, an integer `k`, an integer `x`, and an array `a` of length `n`. It then computes and prints the maximum value of the expression `2 * a[max(i, x) - x] - a[i]` for `i` in the range `n - k` to `n + 1`. The function handles up to `2 * 10^5` elements across all test cases. If `x` is greater than `n`, `max(i, x)` simplifies to `x`. If `k` is larger than `n`, the range `n - k` to `n + 1` becomes invalid, but the function still computes the expression for valid indices within this range.

