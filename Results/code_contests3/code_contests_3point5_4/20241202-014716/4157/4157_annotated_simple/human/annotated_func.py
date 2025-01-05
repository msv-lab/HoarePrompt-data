#State of the program right berfore the function call: n, a, d are integers such that 1 <= n <= 10^5, 1 <= a, d <= 10^6. Each trolleybus has ti and vi integers such that 0 <= t1 < t2... < tn - 1 < tn <= 10^6, 1 <= vi <= 10^6.**
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, the final value of `t` will be the maximum value calculated throughout the loop. `n` is greater than 0, `a` and `d` are integers within the specified ranges, `ti` and `v` hold float values, and `t1` is calculated based on the provided formula.
#Overall this is what the function does:The function `func` does not accept any parameters explicitly. It reads input for `n`, `a`, and `d`, then iterates over `n` trolleybuses to calculate the maximum time `t` based on the provided formulas. The calculated maximum time `t` is printed after each iteration. The function operates on predefined parameters and trolleybus values and returns the maximum time `t` calculated during the iteration process.

