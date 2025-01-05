#State of the program right berfore the function call: n is a positive integer representing the number of trolleybuses (1 ≤ n ≤ 10^5), a is a positive integer representing the maximum acceleration of the trolleybuses (1 ≤ a ≤ 10^6), and d is a positive integer representing the distance from the depot to the final station (1 ≤ d ≤ 10^6). Each trolleybus has a departure time ti (0 ≤ ti ≤ 10^6) and a maximum speed vi (1 ≤ vi ≤ 10^6), with the departure times being strictly increasing.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a positive integer, `d` is a positive integer, `t` is the maximum of all computed values during the iterations or 0.0 if `n` is 0, `i` is equal to `n`.
#Overall this is what the function does:The function reads the number of trolleybuses, their maximum acceleration, and the distance to the final station. For each trolleybus, it calculates the time it takes to reach the station based on its departure time and maximum speed, taking into account the distance and acceleration. It then prints the maximum travel time for each trolleybus. The function does not handle any edge cases related to invalid input or conditions where no trolleybuses are provided, as the inputs are assumed to be valid according to the problem's constraints.

