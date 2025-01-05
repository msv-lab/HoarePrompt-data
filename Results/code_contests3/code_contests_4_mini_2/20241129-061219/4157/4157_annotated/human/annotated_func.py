#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), a is a positive integer (1 ≤ a ≤ 10^6), d is a positive integer (1 ≤ d ≤ 10^6); each trolleybus is defined by a pair of integers ti and vi, where ti is a non-negative integer (0 ≤ ti ≤ 10^6) representing the time the i-th trolleybus leaves the depot, and vi is a positive integer (1 ≤ vi ≤ 10^6) representing the maximum speed of the i-th trolleybus; the sequence of times ti is strictly increasing.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a positive integer, `d` is a positive integer, `t` is the maximum value of all computed `t1 + ti` values across `n` iterations, `i` is `n`, `ti` and `v` are the last input float values, and `t1` is calculated based on the last input values.
#Overall this is what the function does:The function accepts three positive integers `n`, `a`, and `d`, representing the number of trolleybuses, acceleration, and distance respectively. It processes `n` pairs of floats representing the departure time and maximum speed of each trolleybus. For each trolleybus, it calculates a time `t1` based on the given formulas that determine the time taken to cover the distance `d` under acceleration `a` and maximum speed `v`. It keeps track of the maximum computed value of `t1 + ti` across all trolleybuses and prints this value after each iteration. The function does not have a return statement, indicating it only prints results without returning any final value.

