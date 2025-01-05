#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100,000), a is a positive integer representing the maximum acceleration of the trolleybuses (1 ≤ a ≤ 1,000,000), d is a positive integer representing the distance to the final station (1 ≤ d ≤ 1,000,000), and for each trolleybus i, ti is a non-negative integer representing the departure time (0 ≤ ti ≤ 1,000,000) in strictly increasing order, and vi is a positive integer representing the maximum speed (1 ≤ vi ≤ 1,000,000).
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a positive integer, `d` is a positive integer, `t` is the maximum value of all computed `t1 + ti` values across all iterations, `i` is equal to `n`, `ti` and `v` are the last pair of floats read from input before the loop finished executing.
#Overall this is what the function does:The function accepts three integer parameters: `n`, `a`, and `d`, which represent the number of trolleybuses, the maximum acceleration, and the distance to the final station, respectively. It also reads pairs of floats representing the departure time and maximum speed for each trolleybus. For each trolleybus, it calculates a time value based on the maximum speed and acceleration, comparing this to the previous maximum time to determine the latest time a trolleybus can reach the final station. The function outputs the maximum time for each trolleybus, but it does not return any value. It is important to note that the code assumes input is provided correctly and does not handle any potential input errors or edge cases like negative values or out-of-bound values for `ti` and `vi`.

