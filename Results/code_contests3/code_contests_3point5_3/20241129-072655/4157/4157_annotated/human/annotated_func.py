#State of the program right berfore the function call: **Precondition**: 
- n is the number of trolleybuses, where 1 ≤ n ≤ 105.
- a is the maximum acceleration of the trolleybuses, where 1 ≤ a ≤ 10^6.
- d is the distance from the depot to the final station, where 1 ≤ d ≤ 10^6.
- For each trolleybus i (1 ≤ i ≤ n):
    - ti is the time when the trolleybus leaves the depot, where 0 ≤ t1 < t2 < ... < tn - 1 < tn ≤ 10^6.
    - vi is the maximum speed of the trolleybus, where 1 ≤ vi ≤ 10^6.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `t` is the maximum value between `t1 + ti` and the previous value of `t`, `n`, `a`, `d` remain the same as the initial state
#Overall this is what the function does:Functionality: The function `func` reads input for the number of trolleybuses, maximum acceleration, and distance from the depot to the final station. Then, for each trolleybus, it calculates the time required to reach the final station using the given formulas and updates the maximum time taken. The function prints this maximum time for each trolleybus. However, the function lacks a clear output or return value, which might be an oversight in the annotations.

