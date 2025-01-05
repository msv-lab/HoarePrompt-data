#State of the program right berfore the function call: n, a, d are integers such that 1 <= n <= 10^5, 1 <= a, d <= 10^6. Each trolleybus has ti and vi integers such that 0 <= t1 < t2... < tn - 1 < tn <= 10^6, 1 <= vi <= 10^6.**
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 1, `a` and `d` remain unchanged, `t` contains the maximum value of t1 + ti for all iterations, `i` is n-1, `ti` and `v` are assigned the values returned by `map(float, raw_input().split())`, `t1` is calculated based on the condition provided in the code snippet.
#Overall this is what the function does:The function `func` reads inputs for the number of trolleybuses, acceleration, and distance. Then, for each trolleybus, it calculates the time taken to reach the destination based on given formulas. The maximum time taken among all trolleybuses is stored in `t`, but the function does not explicitly return any value.

