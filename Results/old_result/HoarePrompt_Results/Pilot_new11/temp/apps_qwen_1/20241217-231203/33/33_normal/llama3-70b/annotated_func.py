#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and for each i (1 ≤ i ≤ n), t_{i} is an integer such that 1 ≤ t_{i} ≤ 10^6 and dir_{i} is a string representing the direction ("North", "South", "West", "East").
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 50, `t_i` is an integer such that 1 ≤ `t_i` ≤ 10^6 for each i (1 ≤ i ≤ `n`), `dir_i` is a string representing the direction ("North", "South", "West", "East"), `curr_lat` is the final latitude after all valid directions are applied, `curr_lat` is within the range [-90, 90]. If `curr_lat` is 90, `dir` must be 'South' for the loop to continue without termination. If `curr_lat` is -90, `dir` must be 'North' for the loop to continue without termination. If the loop terminates due to invalid conditions, the printed output is 'NO'.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function processes a series of movements in cardinal directions (North, South, West, East) and updates the current latitude accordingly. It ensures that the latitude remains within the valid range of -90 to 90 degrees. If the latitude reaches -90, the next movement must be North; if it reaches 90, the next movement must be South. If any movement results in the latitude exceeding the valid range or violates the above rules, the function prints 'NO' and exits. After processing all movements, if the final latitude is exactly 90 degrees, the function prints 'YES'; otherwise, it prints 'NO'.

