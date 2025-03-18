#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and for each i (1 ≤ i ≤ n), t_{i} is an integer such that 1 ≤ t_{i} ≤ 10^6 and dir_{i} is one of the strings "North", "South", "West", "East".
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
        
    #State of the program after the  for loop has been executed: `n` is at least 0, `curr_lat` is within the range of -90 to 90, the output is 'NO', and the final direction `dir_f` is the last direction received. If `curr_lat` is exactly -90 and the final direction is not 'North', the output is 'NO'. If `curr_lat` is exactly 90 and the final direction is not 'South', the output is 'NO'.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function processes a series of movements in cardinal directions (North, South, West, East) and calculates the resulting latitude. It ensures that the latitude remains within the valid range of -90 to 90 degrees. If at any point the latitude goes out of this range or if the final latitude is exactly -90 and the last movement was not North, or if the final latitude is exactly 90 and the last movement was not South, the function outputs 'NO'. Otherwise, it outputs 'YES'. The function accepts an integer `n` representing the number of movements, and `n` pairs of integers and directions as input. It does not return any value.

