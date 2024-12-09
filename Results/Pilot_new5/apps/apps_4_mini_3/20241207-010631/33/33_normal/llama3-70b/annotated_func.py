#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and each t_i is an integer such that 1 ≤ t_i ≤ 10^6 with corresponding dir_i being one of the strings "North", "South", "West", or "East".
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
        
    #State of the program after the  for loop has been executed: `curr_lat` is between -90 and 90, inclusive; `n` is an integer such that 1 ≤ `n` ≤ 50; all directions are valid strings corresponding to 'North' or 'South'.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 50) and processes `n` pairs of integer `t_i` (1 ≤ t_i ≤ 10^6) and direction strings `dir_i` ("North" or "South"). It updates the variable `curr_lat` to represent the current latitude based on the directions. If the latitude exceeds the bounds of -90 to 90 or if it conditions on reaching the poles are not satisfied, it will print 'NO' and terminate the function. After processing all inputs, it prints 'YES' if the final latitude is exactly 90; otherwise, it prints 'NO'. The function ignores any directions that are "West" or "East".

