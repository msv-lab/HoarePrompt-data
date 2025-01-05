#State of the program right berfore the function call: n is an integer representing the number of trolleybuses (1 ≤ n ≤ 10^5), a is an integer representing the maximum acceleration of the trolleybuses (1 ≤ a ≤ 10^6), d is an integer representing the distance from the depot to the final station (1 ≤ d ≤ 10^6), and for each trolleybus, ti is a non-negative integer representing the time when it leaves the depot (0 ≤ ti ≤ 10^6) and vi is a positive integer representing its maximum speed (1 ≤ vi ≤ 10^6), with the times t1, t2, ..., tn being in strictly increasing order.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `t` is the maximum time calculated for all trolleybuses based on their respective acceleration times and initial times, `i` is equal to `n` after the loop finishes, `ti` and `v` are the last float values read from input during the final iteration, `t1` is the last calculated time based on the final values of `d`, `v`, and `a`.
#Overall this is what the function does:The function accepts integers representing the number of trolleybuses `n`, maximum acceleration `a`, and distance `d` to the station. For each trolleybus, it takes non-negative departure time `ti` and positive maximum speed `vi`. The function calculates the time `t` when each trolleybus reaches the station based on its acceleration and speed, and prints the maximum time taken for all trolleybuses to arrive at the station. It does not return any value; instead, it outputs the arrival times directly. Additionally, it assumes valid input as per the specified constraints.

