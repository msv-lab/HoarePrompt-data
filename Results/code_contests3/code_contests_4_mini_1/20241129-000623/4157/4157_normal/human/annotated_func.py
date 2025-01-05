#State of the program right berfore the function call: n is a positive integer representing the number of trolleybuses (1 ≤ n ≤ 10^5), a is a positive integer representing the maximum acceleration of the trolleybuses (1 ≤ a ≤ 10^6), d is a positive integer representing the distance to the final station (1 ≤ d ≤ 10^6), and for each trolleybus i, ti is a non-negative integer representing the time it leaves the depot (0 ≤ ti ≤ 10^6) and vi is a positive integer representing its maximum speed (1 ≤ vi ≤ 10^6), with the constraint that 0 ≤ t1 < t2 < ... < tn ≤ 10^6.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `t` is the maximum time calculated from all `t1 + ti` values for each trolleybus, `i` is equal to `n`, `ti` is the last input float, `v` is the last input float.
#Overall this is what the function does:The function accepts parameters `n` (number of trolleybuses), `a` (maximum acceleration), and `d` (distance to the final station). For each trolleybus, it also accepts `ti` (departure time) and `vi` (maximum speed). The function calculates the maximum time taken for all trolleybuses to reach the final station based on their speed, acceleration, and departure times. It prints the maximum time for each trolleybus as it processes them. The function does not handle cases where the calculation might result in invalid scenarios (e.g., if `d` is less than or equal to `0`, which is theoretically outside the stated constraints).

