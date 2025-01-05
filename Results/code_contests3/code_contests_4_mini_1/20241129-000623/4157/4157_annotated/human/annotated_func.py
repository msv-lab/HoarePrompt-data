#State of the program right berfore the function call: n is a positive integer representing the number of trolleybuses (1 ≤ n ≤ 10^5), a is a positive integer representing the maximum acceleration of trolleybuses (1 ≤ a ≤ 10^6), d is a positive integer representing the distance to the final station (1 ≤ d ≤ 10^6), and for each trolleybus i (1 ≤ i ≤ n), ti (0 ≤ ti ≤ 10^6) is the time when it leaves the depot and vi (1 ≤ vi ≤ 10^6) is its maximum speed, with the condition that 0 ≤ t1 < t2 < ... < tn.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `t` is the maximum of all computed values from `t1 + ti` over all iterations, `n` is a non-negative integer, `a` is an input integer, `d` is an input integer.
#Overall this is what the function does:The function accepts implicit parameters related to trolleybuses including the number of trolleybuses (`n`), maximum acceleration (`a`), distance to the final station (`d`), and for each trolleybus, its departure time (`ti`) and maximum speed (`vi`). The function calculates the time taken for each trolleybus to reach the final station based on its acceleration and speed, and prints the maximum arrival time among all trolleybuses. It handles cases where the distance allows for a straightforward calculation or requires the use of kinematic equations, but does not explicitly return any value. Therefore, the function effectively computes and displays the maximum time required for all trolleybuses to arrive at the station.

