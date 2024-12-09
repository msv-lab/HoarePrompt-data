#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 50, and for each i from 1 to n, t_i is a positive integer (1 ≤ t_i ≤ 10^6) and dir_i is a string that is either "North", "South", "West", or "East".
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 50; `curr_lat` is within the range of -90 to 90, adjusted based on the inputs processed during the loop iterations; `t` is an integer representing the last valid input value converted from the input; if `curr_lat` reaches -90, the last direction must be 'North' to maintain it; if `curr_lat` reaches 90, the last direction must be 'South' to maintain it.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function accepts a number of directional inputs and distance values, processing them to adjust a latitude value starting from 90 degrees. It checks to ensure that the latitude does not exceed the range of -90 to 90 degrees based on the input directions ('North' or 'South'). If the latitude reaches -90, the last direction must be 'North', and if it reaches 90, the last direction must be 'South'. If any of these conditions are violated, the function outputs 'NO'. After processing all inputs, it prints 'YES' if the final latitude is exactly 90; otherwise, it prints 'NO'.

