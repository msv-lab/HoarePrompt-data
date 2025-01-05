#State of the program right berfore the function call: n, a, and d are integers such that 1 <= n <= 10^5, 1 <= a, d <= 10^6. Each trolleybus's time ti and maximum speed vi are integers such that 0 <= t1 < t2 < ... < tn-1 < tn <= 10^6, 1 <= vi <= 10^6.**
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `t` is the maximum value between all the calculated `t1 + ti` values in each iteration of the loop, `i` is equal to n-1, `n` is unchanged, `ti` and `v` are float values from input splitting, `t1` is calculated based on the conditions provided in the code snippet
#Overall this is what the function does:The function `func` reads input values for `n`, `a`, and `d`, then iterates `n` times to calculate `t1` based on the provided formulas. It finds the maximum value of `t1 + ti` in each iteration and prints it. The function does not have a specified return value. Edge cases and missing functionality include the requirement for the `math` module not being imported, and the absence of error handling for invalid inputs.

