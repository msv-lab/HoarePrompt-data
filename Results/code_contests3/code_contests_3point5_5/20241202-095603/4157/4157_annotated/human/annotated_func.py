#State of the program right berfore the function call: **Precondition**: 

- n is an integer such that 1 ≤ n ≤ 10^5.
- a is an integer such that 1 ≤ a ≤ 10^6.
- d is an integer such that 1 ≤ d ≤ 10^6.
- For each trolleybus i (1 ≤ i ≤ n):
  - ti is an integer such that 0 ≤ t1 < t2 < ... < tn - 1 < tn ≤ 10^6.
  - vi is an integer such that 1 ≤ vi ≤ 10^6.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `t` is the maximum value calculated throughout all iterations of the loop
#Overall this is what the function does:The function `func` reads input values for n, a, and d. Then, for each trolleybus i, it calculates the time t1 based on the provided formula and updates the maximum time value t throughout all iterations. The function prints the maximum time calculated for each trolleybus. The function does not return any value.

