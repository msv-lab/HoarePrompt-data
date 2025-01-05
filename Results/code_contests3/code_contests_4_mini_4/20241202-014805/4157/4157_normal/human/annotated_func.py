#State of the program right berfore the function call: n is a positive integer representing the number of trolleybuses (1 ≤ n ≤ 10^5), a is a positive integer representing the maximum acceleration of the trolleybuses (1 ≤ a ≤ 10^6), d is a positive integer representing the distance from the depot to the final station (1 ≤ d ≤ 10^6), and for each trolleybus, ti is a non-negative integer representing the time it leaves the depot (0 ≤ ti ≤ 10^6) and vi is a positive integer representing its maximum speed (1 ≤ vi ≤ 10^6) such that the times are strictly increasing (0 ≤ t1 < t2 < ... < tn).
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a positive integer, `d` is a positive integer, `t` is the maximum of all computed times across the trolleybuses, and `i` is `n-1`.
#Overall this is what the function does:The function accepts three positive integers: `n` (the number of trolleybuses), `a` (the maximum acceleration), and `d` (the distance to the final station), followed by `n` pairs of non-negative integers `ti` (departure times) and positive integers `vi` (maximum speeds) for each trolleybus. It calculates the time required for each trolleybus to reach the final station based on its departure time and speed, considering the acceleration, and prints the maximum time taken by any trolleybus to reach the station. If the distance can be covered with the given speed and acceleration, it computes the appropriate time; otherwise, it uses a different formula. The function does not explicitly return a value, but it outputs the maximum time for each trolleybus sequentially.

