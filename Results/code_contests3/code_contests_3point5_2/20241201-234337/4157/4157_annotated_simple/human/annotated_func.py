#State of the program right berfore the function call: **Precondition**: 
- n is a positive integer representing the number of trolleybuses.
- a is a positive integer representing the maximum acceleration of the trolleybuses.
- d is a positive integer representing the distance from the depot to the final station.
- ti is a non-decreasing sequence of integers representing the time when each trolleybus leaves the depot.
- vi is a positive integer representing the maximum speed of each trolleybus.
def func():
    t = 0.0
    n, a, d = map(int, raw_input().split())
    for i in xrange(n):
        ti, v = map(float, raw_input().split())
        
        t1 = v / a + (d - v * v / (2 * a)) / v if d > v * v / (2 * a) else math.sqrt(
            2 * d / a)
        
        t = max(t1 + ti, t)
        
        print(t)
        
    #State of the program after the  for loop has been executed: `t` is the maximum value between `t1 + ti` and the previous value of `t` after all iterations of the loop have finished
#Overall this is what the function does:The function accepts no parameters explicitly but reads input from the user. It calculates the minimum time required for all trolleybuses to reach the final station without violating any speed limits. The function iterates through the trolleybuses, calculates the travel time for each trolleybus based on its speed and distance, and updates the maximum time needed.

