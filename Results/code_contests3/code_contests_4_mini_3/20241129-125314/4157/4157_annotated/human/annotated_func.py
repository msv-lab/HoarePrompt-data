#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), a is a positive integer representing the maximum acceleration (1 ≤ a ≤ 10^6), d is a positive integer representing the distance to the final station (1 ≤ d ≤ 10^6), and each trolleybus has a departure time ti (0 ≤ ti ≤ 10^6) and a maximum speed vi (1 ≤ vi ≤ 10^6) such that the departure times are in strictly increasing order.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `t` is the maximum value calculated from the expression involving `t1 + ti` across all iterations, `n` is a positive integer indicating the number of iterations, `a` is a positive integer, `d` is a positive integer.
#Overall this is what the function does:The function reads input values for the number of trolleybuses `n`, maximum acceleration `a`, and distance `d`. It then processes each trolleybus's departure time `ti` and maximum speed `vi` to calculate the time `t` it takes for each trolleybus to reach the final station based on physics equations. The function prints the maximum time across all trolleybuses, considering their departure times and calculated travel times. The function does not directly accept parameters but relies on input values, which may lead to errors if the input format is incorrect or if `d` is less than the distance each trolleybus can travel based on its speed.

