#State of the program right berfore the function call: 
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: The final value of `t` after all iterations of the loop have finished.
#Overall this is what the function does:The function `func` reads input values for `n`, `a`, and `d`, then iterates `n` times to calculate and update the value of `t`. It computes `t` based on the input values and prints the updated value of `t` after each iteration. The function does not accept any parameters and does not return any value.

