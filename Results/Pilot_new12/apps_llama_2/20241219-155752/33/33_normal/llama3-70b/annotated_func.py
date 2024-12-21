#State of the program right berfore the function call: The input consists of a sequence of instructions where each instruction is a pair (t, dir) with t being an integer representing the distance to travel and dir being a string representing the direction of travel, which can be one of "North", "South", "West", "East". The sequence starts from the North Pole and consists of n instructions, where n is an integer between 1 and 50, inclusive. The distance t for each instruction is an integer between 1 and 10^6, inclusive.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 0 and 50, inclusive, `curr_lat` is the final latitude after updating the original value of 90 based on the directions and distances of travel, unless the program has exited and printed 'NO' due to `curr_lat` being outside the valid range or reaching a boundary latitude with an invalid direction.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function accepts a sequence of instructions where each instruction is a pair of distance and direction, processes these instructions starting from the North Pole, and determines whether the final latitude is back at the North Pole (90 degrees) or not. The function takes into account the distance and direction of travel, updating the latitude accordingly, and checks for invalid movements such as traveling beyond the valid latitude range (-90 to 90 degrees) or reaching a boundary latitude with an invalid direction. If any invalid movement is detected, the function immediately prints 'NO' and exits. Otherwise, after processing all instructions, the function prints 'YES' if the final latitude is 90 degrees (i.e., back at the North Pole) and 'NO' otherwise. The function ignores any instructions with a direction other than 'North' or 'South'.

