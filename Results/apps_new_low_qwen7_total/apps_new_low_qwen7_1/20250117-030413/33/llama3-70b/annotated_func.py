#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and for each i from 1 to n, t_{i} is an integer such that 1 ≤ t_{i} ≤ 10^6 and dir_{i} is one of the strings "North", "South", "West", "East".
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
        
    #State of the program after the  for loop has been executed: `curr_lat` is within the valid range [-90, 90], `n` is equal to the number of times the loop was executed, `t` is an integer representing the last distance traveled, `dir` is a string representing the direction of the last movement, provided that no exit conditions were met. If `curr_lat` is 90, `dir` must be 'South'. If `curr_lat` is -90, `dir` must be 'North'.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function processes a series of movements in cardinal directions (North, South, West, East) and calculates the resulting latitude. It ensures that the calculated latitude remains within the valid geographic range of -90 to 90 degrees. If the latitude exceeds these bounds or if certain invalid conditions occur during the process, the function prints 'NO' and exits. Otherwise, it prints 'YES' indicating that the final latitude is within the valid range. The function does not return any value.

