#State of the program right berfore the function call: n is a positive integer representing the number of trolleybuses (1 ≤ n ≤ 10^5), a is a positive integer representing the maximum acceleration of the trolleybuses (1 ≤ a ≤ 10^6), d is a positive integer representing the distance to the final station (1 ≤ d ≤ 10^6), and each of the next n lines contains two integers ti and vi (where 0 ≤ ti ≤ 10^6 and 1 ≤ vi ≤ 10^6) representing the departure time and maximum speed of the i-th trolleybus, respectively.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a positive integer, `d` is a positive integer, `t` is the maximum of all computed values of `t1 + ti` across all iterations, where each `ti` and `v` are input floats provided during the loop execution.
#Overall this is what the function does:The function accepts three positive integers `n`, `a`, and `d`, where `n` represents the number of trolleybuses, `a` is the maximum acceleration, and `d` is the distance to the final station. For each trolleybus, it reads its departure time `ti` and maximum speed `vi`. It computes the time `t1` required for each trolleybus to reach the station based on its speed, acceleration, and the distance. The function then keeps track of the maximum time across all trolleybuses, which is printed for each iteration. Ultimately, it outputs the maximum computed time for all trolleybuses, which could include edge cases such as when the distance is less than or equal to the distance each trolleybus can travel before reaching the maximum speed. The function does not handle invalid input cases or potential errors in the input format.

