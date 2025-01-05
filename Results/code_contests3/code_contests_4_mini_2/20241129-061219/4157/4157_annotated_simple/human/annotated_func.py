#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), a is a positive integer representing the maximum acceleration (1 ≤ a ≤ 10^6), d is a positive integer representing the distance to the final station (1 ≤ d ≤ 10^6), and for each trolleybus, ti is a non-negative integer representing the time of departure (0 ≤ ti ≤ 10^6) and vi is a positive integer representing the maximum speed (1 ≤ vi ≤ 10^6); the times ti are strictly increasing for each trolleybus.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a positive integer, `d` is a positive integer, `t` is the maximum time computed from all iterations, and `t` is greater than or equal to 0.0.
#Overall this is what the function does:The function accepts three positive integers `n` (the number of trolleybuses), `a` (the maximum acceleration), and `d` (the distance to the final station). It then processes `n` pairs of values representing the departure time `ti` and maximum speed `vi` of each trolleybus. For each trolleybus, it calculates the time it takes to reach the final station based on its speed and the distance, considering the acceleration. The function returns the maximum time computed from all trolleybuses, which represents when the last trolleybus reaches the final station. However, there is no explicit return statement in the code; it only prints the times instead of returning a value. Therefore, the actual behavior of the function does not align with the expected return of the last trolleybus's arrival time.

