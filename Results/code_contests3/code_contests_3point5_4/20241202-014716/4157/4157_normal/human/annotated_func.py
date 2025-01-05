#State of the program right berfore the function call: n, a, and d are positive integers such that 1 ≤ n ≤ 10^5, 1 ≤ a, d ≤ 10^6. Each trolleybus's time ti and maximum speed vi are non-negative integers such that 0 ≤ t1 < t2 < ... < tn ≤ 10^6, 1 ≤ vi ≤ 10^6.**
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 1, `a` and `d` have integer values from user input, `t` is updated to the maximum value between `t1 + ti` and the current `t` for all iterations of the loop, `i` is `n - 1`, `ti` and `v` have float values from user input for the last iteration, `t1` is determined based on certain conditions for the last iteration, and the final value of `t` is printed
#Overall this is what the function does:The function `func` reads inputs for the number of trolleybuses and their corresponding time and speed values. For each trolleybus, it calculates the time it takes to reach a certain distance based on acceleration and then updates the maximum time taken among all trolleybuses. The function does not accept any parameters and does not return any value.

