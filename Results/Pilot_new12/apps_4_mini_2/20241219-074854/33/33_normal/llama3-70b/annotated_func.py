#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and for each part of the journey described by an integer t_i (1 ≤ t_i ≤ 10^6) and a string dir_i which is one of {"North", "South", "West", "East"}.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 50; `curr_lat` is a latitude value that may change based on the inputs 't' and 'dir' received during the loop iterations, remaining within the bounds of -90 and 90. If `curr_lat` exceeds these bounds, 'NO' is printed, and the program exits. If `curr_lat` is 90, the last valid direction must be 'South' to avoid printing 'NO' and exiting. If `curr_lat` is -90, the last valid direction must be 'North' for the same reason. The values of 't' and 'dir' are determined by user input during each iteration of the loop.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function takes an integer input `n` representing the number of journey parts, where each part includes a distance `t` and a direction `dir` that can be "North", "South", "West", or "East". It calculates a cumulative latitude `curr_lat` starting from 90 degrees, adjusting it based on the distances for the specified directions. It only modifies `curr_lat` for "North" and "South" directions, while "West" and "East" directions are ignored. The function checks if `curr_lat` remains within the bounds of -90 to 90 degrees, printing 'NO' and exiting if it exceeds these limits or if it reaches the boundary values (-90 or 90) without the appropriate direction. After processing all journey parts, it prints 'YES' if `curr_lat` equals 90, otherwise 'NO'. The function does not handle invalid or malformed inputs, which could lead to exceptions if not controlled.

