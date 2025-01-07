#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and for each of the next n lines, t_i is an integer such that 1 ≤ t_i ≤ 10^6 and dir_i is a string that is either "North", "South", "West", or "East".
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 50; `curr_lat` is a value between -90 and 90, inclusive, representing the final latitude after all iterations. The loop has executed `n` times, modifying `curr_lat` based on the provided inputs for `t` and `dir`. If any conditions (such as exceeding latitude boundaries or invalid direction inputs) caused the program to terminate early, 'NO' would have been printed, and `curr_lat` would be unchanged from its previous state.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 50) and for `n` iterations expects an integer `t` (1 ≤ t ≤ 10^6) and a direction (`dir`) which can be "North", "South", "West", or "East". The function calculates a cumulative latitude based on `t` and the specified direction, modifying `curr_lat` accordingly. If during any modification, `curr_lat` exceeds the boundaries (-90 or 90) or does not meet specific conditions for reaching the poles, it prints 'NO' and terminates. After all iterations, it prints 'YES' if `curr_lat` equals 90, otherwise it prints 'NO'. The function ignores any inputs with directions "West" or "East", which could lead to missing updates in latitude, and does not handle invalid inputs gracefully, which could raise an error if the input does not fit expected parameters.

