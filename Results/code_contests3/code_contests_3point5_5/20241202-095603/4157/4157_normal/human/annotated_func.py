#State of the program right berfore the function call: **Precondition**: 
- n is an integer representing the number of trolleybuses, where 1 <= n <= 10^5.
- a is an integer representing the maximum acceleration of the trolleybuses, where 1 <= a <= 10^6.
- d is an integer representing the distance from the depot to the final station, where 1 <= d <= 10^6.
- Each of the n following lines contains two integers ti and vi, where 0 <= t1 < t2 < ... < tn-1 < tn <= 10^6 and 1 <= vi <= 10^6, representing the time when the trolleybus leaves the depot and its maximum speed, respectively.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `t` is the maximum value between the calculated value and the current value after all iterations of the loop have executed. `n`, `a`, `d` are assigned integer inputs from user input, `i` is `n`, `ti` and `v` are assigned float values from input, `t1` is assigned a float value based on the given conditional expression
#Overall this is what the function does:The function does not accept any parameters. It reads input values for the number of trolleybuses, maximum acceleration, and distance to the final station. Then, for each trolleybus, it calculates the minimum time required to reach the final station based on certain conditions. The function outputs the maximum time among all trolleybuses. However, the code is missing the import statement for the math module, which may cause an error when trying to use the sqrt function.

