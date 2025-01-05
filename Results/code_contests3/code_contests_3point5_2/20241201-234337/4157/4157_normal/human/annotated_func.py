#State of the program right berfore the function call: n, a, and d are positive integers such that 1 <= n <= 10^5, 1 <= a, d <= 10^6. Each trolleybus i (1 <= i <= n) has two integers ti and vi, where 0 <= t1 < t2 < ... < tn-1 < tn <= 10^6 and 1 <= vi <= 10^6.**
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `t` contains the maximum value achieved during the iterations of the loop, `n`, `a`, and `d` retain their initial assigned integer values, `ti` and `v` have float values assigned from the input, `t1` is calculated based on the conditions provided in the loop
#Overall this is what the function does:The function calculates the total time taken by n trolleybuses to travel a distance d based on their individual time and speed values. It iterates through the trolleybuses, calculates the time taken by each bus to reach the destination, and keeps track of the maximum time taken among all buses. The function outputs the maximum time taken. However, the code is missing the import statement for the math module, so it will raise an error when trying to use math.sqrt. Additionally, the code does not handle any input validation or error checking, assuming correct input format and values.

