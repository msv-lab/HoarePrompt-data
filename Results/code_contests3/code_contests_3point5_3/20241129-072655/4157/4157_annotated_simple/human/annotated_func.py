#State of the program right berfore the function call: **Precondition**: **n, a, and d are positive integers such that 1 ≤ n ≤ 10^5, 1 ≤ a, d ≤ 10^6. Each ti is a non-negative integer such that 0 ≤ t1 < t2 < ... < tn ≤ 10^6, and vi is a positive integer such that 1 ≤ vi ≤ 10^6.**
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `t` will contain the maximum value between `t1 + ti` and the current value of `t`, `n`, `a`, `d` will have the final integer values based on user input, `i` will be equal to `n-1`, `ti` and `v` will be the float values from the last iteration of the loop.
#Overall this is what the function does:The function reads input values for the number of visitors, arrival time, and departure time. It calculates the maximum total time each visitor spends in the system and prints this value. The function does not return the total number of visitors as indicated in the annotations.

