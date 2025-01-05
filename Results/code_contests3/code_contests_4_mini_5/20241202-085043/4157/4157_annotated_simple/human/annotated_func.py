#State of the program right berfore the function call: n is a positive integer representing the number of trolleybuses (1 ≤ n ≤ 10^5), a is a positive integer representing the maximum acceleration of the trolleybuses (1 ≤ a ≤ 10^6), d is a positive integer representing the distance from the depot to the final station (1 ≤ d ≤ 10^6), and for each trolleybus, ti is a non-negative integer representing the time it leaves the depot (0 ≤ ti ≤ 10^6) and vi is a positive integer representing its maximum speed (1 ≤ vi ≤ 10^6), with the constraint that the sequence of times satisfies 0 ≤ t1 < t2 < ... < tn ≤ 10^6.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a positive integer, `d` is a positive integer, `t` is the maximum of all calculated values of `t1 + ti` from each iteration, `i` is equal to `n`, `ti` and `v` are the last float input values from the final iteration, and `t1` is determined based on the last input values of `d`, `v`, and `a`.
#Overall this is what the function does:The function reads values for the number of trolleybuses `n`, maximum acceleration `a`, and distance `d`. For each trolleybus, it takes the departure time `ti` and maximum speed `vi`, then calculates the time it takes for each trolleybus to reach the final station based on its speed and the given acceleration. The function keeps track of the maximum time encountered across all trolleybuses and prints this maximum value after processing each trolleybus. The calculations also handle cases where the distance is less than or equal to the distance that can be covered under constant acceleration. The function does not handle any edge cases related to invalid input values or scenarios where the inputs do not meet the specified constraints.

