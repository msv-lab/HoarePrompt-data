#State of the program right berfore the function call: **Precondition**: **n, a, d are positive integers such that 1 <= n <= 10^5, 1 <= a, d <= 10^6. Each ti is a non-negative integer, vi is a positive integer, and t1 < t2 < ... < tn-1 < tn.**
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `t` is a floating-point number, `n` is greater than 0, `a` and `d` are integer values obtained from the input, `ti` and `v` are assigned floating-point values based on user input, `t1` is calculated based on the user input values of `v`, `a`, and `d`, and `t` is updated accordingly, and the final value of `t` is the maximum value calculated throughout all iterations of the loop.
#Overall this is what the function does:The function `func` reads input values for `n`, `a`, and `d`, then iterates `n` times to calculate a time value `t` based on user input. It computes `t1` based on certain conditions and updates `t` to the maximum value calculated during the loop. The function prints the final `t` value. The function does not return any value explicitly.

