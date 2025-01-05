#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100,000), a is a positive integer representing the maximum acceleration (1 ≤ a ≤ 1,000,000), d is a positive integer representing the distance to the final station (1 ≤ d ≤ 1,000,000), and for each trolleybus i (1 ≤ i ≤ n), ti is a non-negative integer representing the time when the i-th trolleybus leaves the depot (0 ≤ ti ≤ 1,000,000) and vi is a positive integer representing the maximum speed of the i-th trolleybus (1 ≤ vi ≤ 1,000,000) with the condition that the departure times are strictly increasing (0 ≤ t1 < t2 < ... < tn ≤ 1,000,000).
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer; `a` is an input integer; `d` is an input integer; `t` is the maximum value of all computed `t1 + ti` during the loop iterations; `i` is `n-1` after the loop executes; `ti` is the last float from the input; `v` is the last float from the input; `t1` is the last computed value using the formula involving `a`, `d`, and `v`.
#Overall this is what the function does:The function accepts a positive integer `n`, a positive integer `a`, a positive integer `d`, and a list of tuples (ti, vi) for each trolleybus, where `ti` is the departure time and `vi` is the maximum speed. It calculates and prints the time taken for each trolleybus to reach the final station based on their respective departure times and speeds using the provided physics equations. The function does not return any value; it only prints the computed times. The calculations consider the acceleration and the distance to determine the time for each trolleybus, taking into account the maximum speed and whether the distance allows for a straightforward acceleration to that speed.

