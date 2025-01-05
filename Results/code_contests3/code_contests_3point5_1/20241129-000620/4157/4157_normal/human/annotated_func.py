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
        
    #State of the program after the  for loop has been executed: t is the maximum value calculated based on the given formula, n is greater than or equal to 0, a and d have assigned integer values from input, ti is a float, v is a float
#Overall this is what the function does:The function `func` reads integer values `n`, `a`, and `d` from the input. It then iterates `n` times, reading float values `ti` and `v` in each iteration. For each iteration, it calculates `t1` based on the given formula and updates the maximum value of `t`. The function prints the updated `t` value after each iteration. The function does not accept any parameters and does not return any value.

