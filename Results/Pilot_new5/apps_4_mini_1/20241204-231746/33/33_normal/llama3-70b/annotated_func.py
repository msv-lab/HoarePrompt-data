#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 50, and each of the n parts consists of a non-negative integer t_i (1 ≤ t_i ≤ 10^6) and a string dir_i where dir_i is one of {"North", "South", "West", "East"}.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer (1 ≤ n ≤ 50), `curr_lat` remains within the valid latitude range of -90 to 90 after all iterations, and `dir` is a string that indicates the final direction inputted during the loop. If any condition leads to an invalid latitude, the program would have printed 'NO' and exited before completing all iterations.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 50), representing the number of directional movements. For each movement, it reads a non-negative integer `t_i` (1 ≤ t_i ≤ 10^6) and a direction (`dir_i`) which can be "North", "South", "West", or "East". The function adjusts the current latitude based on the direction and distance, ensuring that the latitude remains within the bounds of -90 to 90. If any movement results in an invalid latitude, or if the conditions for reaching latitudes -90 or 90 are not met with the appropriate direction, it prints 'NO' and exits. If the loop completes successfully and the latitude equals 90, it prints 'YES'; otherwise, it prints 'NO'. The function does not return a value but outputs results directly to the console.

