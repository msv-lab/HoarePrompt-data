#State of the program right berfore the function call: **
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `t` has been updated to the maximum value between all the calculated `t1 + ti` values during each iteration of the loop
#Overall this is what the function does:The function reads input values for `n`, `a`, and `d`, then iterates `n` times to calculate `t1` based on the input values. It updates `t` to the maximum value of all calculated `t1 + ti` values during each iteration. The function prints the updated `t` value after each iteration.

