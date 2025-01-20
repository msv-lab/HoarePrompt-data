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
        
    #State of the program after the  for loop has been executed: `t` is a list of integers, `dir` is a list of strings, `curr_lat` is 90, `n` is the final value of the loop variable.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function processes a series of movements (North, South, East, West) represented by distances and directions. Each movement updates the latitude (`curr_lat`), which starts at 90 degrees. If at any point the latitude goes out of the valid range (-90 to 90 degrees), or if the latitude reaches the extreme values (-90 or 90) with an invalid direction, the function prints 'NO' and exits. After processing all movements, if the final latitude is exactly 90 degrees, the function prints 'YES'; otherwise, it prints 'NO'. This function ensures that the final latitude remains within the valid geographical range and correctly handles all possible edge cases.

