#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), a is a positive integer (1 ≤ a ≤ 10^6), d is a positive integer (1 ≤ d ≤ 10^6), and for each trolleybus, ti is a non-negative integer (0 ≤ ti ≤ 10^6) representing the time it leaves the depot, and vi is a positive integer (1 ≤ vi ≤ 10^6) representing its maximum speed, where the sequence of ti values is strictly increasing.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 10^5), `a` is a positive integer (1 ≤ a ≤ 10^6), `d` is a positive integer (1 ≤ d ≤ 10^6), `t` is the maximum of all computed values `t1 + ti` over all iterations, `i` is `n - 1`, `ti` and `v` are the last values read from input.
#Overall this is what the function does:The function reads a positive integer `n` and two additional positive integers `a` and `d` from input. It then iterates `n` times, reading pairs of non-negative integer `ti` (departure time) and positive integer `vi` (maximum speed) for each iteration. For each trolleybus, it computes a time `t1` based on the equations involving `a`, `d`, and `v`, and updates the maximum time `t` encountered during the iterations. After processing all trolleybuses, it prints the maximum time `t` for each trolleybus but does not return any value.

