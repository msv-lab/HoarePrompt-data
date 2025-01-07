#State of the program right berfore the function call: The input is a sequence of movements, each consisting of a non-negative integer distance (t) and a direction (dir) that is one of: "North", "South", "West", "East", where 1 ≤ t ≤ 10^6, and there are 1 ≤ n ≤ 50 such movements.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 50, `t` is the distance of the last movement, `dir` is the direction of the last movement, `curr_lat` is the final latitude after all movements, and if `curr_lat` is within the range [-90, 90], it is updated based on the directions and distances of all movements, otherwise, the program has printed 'NO' and terminated.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function simulates a sequence of 1 to 50 movements with distances between 1 and 10^6 in the "North", "South", "West", or "East" directions, ignoring "West" and "East" movements, and checks if the resulting latitude is equal to 90 after accounting for valid "North" and "South" movements, printing "YES" if the final latitude is 90 and "NO" otherwise, while also handling invalid pole movements and out-of-bounds latitudes by printing "NO" and exiting

