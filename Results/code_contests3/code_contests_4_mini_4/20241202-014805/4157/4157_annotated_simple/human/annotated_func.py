#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5) representing the number of trolleybuses; a is a positive integer (1 ≤ a ≤ 10^6) representing the maximum acceleration of the trolleybuses; d is a positive integer (1 ≤ d ≤ 10^6) representing the distance from the depot to the final station; each of the next n lines contains ti and vi, where ti is a non-negative integer (0 ≤ ti ≤ 10^6) representing the departure time of the i-th trolleybus, and vi is a positive integer (1 ≤ vi ≤ 10^6) representing the maximum speed of the i-th trolleybus, with the constraint that the sequence of departure times is strictly increasing (0 ≤ t1 < t2 < ... < tn).
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `t` is the maximum time calculated from all inputs, `i` is `n-1` after the last iteration, `ti` is the last float from input, `v` is the last float from input.
#Overall this is what the function does:The function processes input data related to multiple trolleybuses, including their departure times, maximum speeds, and the distance from the depot to the final station. It calculates the maximum time taken for all trolleybuses to reach the final station based on their acceleration and speed. The function prints the maximum time for each trolleybus as it processes the input sequentially. It does not accept parameters directly in its signature, instead reading input values from standard input.

