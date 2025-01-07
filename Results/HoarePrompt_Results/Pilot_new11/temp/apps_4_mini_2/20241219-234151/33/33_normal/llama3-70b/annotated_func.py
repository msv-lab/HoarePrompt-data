#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and for each journey part, t_i is an integer such that 1 ≤ t_i ≤ 10^6 and dir_i is one of the strings "North", "South", "West", or "East".
def func():
    n = int(input())
    curr_lat = 90
    for _ in range(n):
        t, dir = input().split()
        
        t = int(t)
        
        if dir == 'North':
            curr_lat += t / 111.195
        elif dir == 'South':
            curr_lat -= t / 111.195
        else:
            continue
        
        if curr_lat < -90 or curr_lat > 90:
            print('NO')
            exit()
        
        if curr_lat == -90 and dir != 'North':
            print('NO')
            exit()
        
        if curr_lat == 90 and dir != 'South':
            print('NO')
            exit()
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 50; `curr_lat` is in the range of -90 to 90; if `curr_lat` is 90, then the input direction must have been 'South' at least once; if `curr_lat` is -90, the input direction must have been 'North' at least once; the program executes without termination, meaning neither 'NO' was printed during execution nor did the program exit prematurely.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function accepts an integer `n` representing the number of journey parts, followed by `n` pairs of inputs consisting of an integer `t` (representing distance in meters) and a direction string (`dir`) that can be "North", "South", "West", or "East". It updates the current latitude based on movements in the North and South directions, ignoring movements in the West and East. The latitude change is calculated using the approximation that 1 degree of latitude is equivalent to roughly 111,195 meters. 

After processing all journey parts, it checks whether the latitude remains within the valid bounds of -90 to 90 degrees. If any direction causes the latitude to exceed these bounds, or if the final latitude is either 90 or -90 without having moved appropriately in the opposite direction at least once, it prints 'NO' and exits the function. If the latitude remains within bounds and the necessary conditions are met for extreme latitudes, it prints 'YES' if the current latitude is 90, otherwise it prints 'NO'. 

Potential edge cases include:
- Ignoring any journey parts with directions other than "North" or "South".
- Only printing 'YES' if the ending latitude is exactly 90 and it confirms the necessary path taken; otherwise, it results in 'NO'.
- Any invalid movements that cause premature termination (i.e., when current latitude goes out of bounds during the journey processing).

