#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50. For each i from 1 to n, t_{i} is an integer such that 1 ≤ t_{i} ≤ 10^6, and dir_{i} is one of "North", "South", "West", "East".
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
        
    #State of the program after the  for loop has been executed: `n` is 0, `curr_lat` is 90.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function processes a series of movements (each defined by a distance `t_i` and direction `dir_i`) starting from a latitude of 90 degrees. It updates the latitude based on the direction and distance of each movement. If at any point the latitude goes out of the valid range [-90, 90] degrees or reaches exactly -90 or 90 degrees with an invalid direction, the function immediately prints 'NO' and exits. After processing all movements, if the final latitude is exactly 90 degrees, the function prints 'YES'; otherwise, it prints 'NO'. The function implicitly accepts an integer `n` (the number of movements) and arrays of integers `t_i` and strings `dir_i` as inputs, even though these are not passed as parameters. Potential edge cases include reaching the boundary latitudes (-90 or 90) with directions other than "North" or "South", respectively.

