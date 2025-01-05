#State of the program right berfore the function call: n, a, and d are integers such that 1 <= n <= 10^5, 1 <= a, d <= 10^6. Each trolleybus has ti and vi as integers where 0 <= t1 < t2 < ... < tn-1 < tn <= 10^6 and 1 <= vi <= 10^6.**
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: At the end of the loop, `t` will contain the maximum value of `t1 + ti` that was calculated during each iteration of the loop. All other variables (`ti`, `v`, `n`, `a`, `d`) are unchanged.
#Overall this is what the function does:The function `func` reads input values for the number of trolleybuses `n`, acceleration `a`, and distance to travel `d`. It then iterates over each trolleybus, calculates the total time taken for each trolleybus to reach the destination based on its velocity and acceleration, and updates the maximum time `t`. The function prints the maximum time `t` after each iteration. The functionality does not handle any error cases related to invalid inputs or exceptions that might occur during the calculations.

