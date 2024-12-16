#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and for each i from 1 to n, t_{i} is an integer such that 1 ≤ t_{i} ≤ 10^6, and dir_{i} is one of the strings "North", "South", "West", "East".
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
        
    #State of the program after the  for loop has been executed: `curr_lat` is within the range \([-90, 90]\), `n` is a non-negative integer, `t_i` is an integer such that \(1 \leq t_i \leq 10^6\), `dir_i` is one of the strings "North", "South", "West", "East". If `curr_lat` is 90 and `dir_i` is not "South" at any point, 'NO' is printed to the console. Similarly, if `curr_lat` is -90 and `dir_i` is not "North" at any point, 'NO' is printed to the console. Otherwise, the final value of `curr_lat` is the result of the cumulative effect of all valid movements (North or South) within the specified range.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function processes a series of movements defined by integers and direction strings, where the latitude changes based on the movement direction and distance. It checks if the final latitude is exactly 90° North or not, and prints 'YES' if the latitude is 90° North, and 'NO' if it is not, considering potential edge cases like exceeding the latitude limits (-90° to 90°) or invalid directions.

