#State of the program right berfore the function call: n is a positive integer representing the number of trolleybuses (1 ≤ n ≤ 10^5), a is a positive integer representing the maximum acceleration of the trolleybuses (1 ≤ a ≤ 10^6), d is a positive integer representing the distance to the final station (1 ≤ d ≤ 10^6), and each trolleybus has a departure time ti (0 ≤ ti ≤ 10^6) and maximum speed vi (1 ≤ vi ≤ 10^6), with the departure times sorted in increasing order (0 ≤ t1 < t2 < ... < tn).
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a positive integer, `d` is a positive integer, `t` is the maximum time taken for all trolleybuses to reach the final station considering their departure times and speeds.
#Overall this is what the function does:The function accepts parameters `n` (the number of trolleybuses), `a` (the maximum acceleration), and `d` (the distance to the final station), along with a list of departure times `ti` and maximum speeds `vi` for each trolleybus. It calculates the maximum time taken for all trolleybuses to reach the final station based on their departure times and speeds. The result is printed for each trolleybus, which represents the time of arrival at the station. The function assumes valid input as per the constraints, but does not handle cases where the distance `d` is less than or equal to zero, which could lead to errors in calculations.

