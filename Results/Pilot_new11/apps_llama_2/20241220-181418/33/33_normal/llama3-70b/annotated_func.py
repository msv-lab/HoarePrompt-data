#State of the program right berfore the function call: n is a positive integer, 1 ≤ n ≤ 50, and for each i-th part of the journey, t_{i} is a positive integer, 1 ≤ t_{i} ≤ 10^6, and dir_{i} is one of the strings: "North", "South", "West", "East".
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `t` is an integer if `n` is positive, `dir` is a direction string if `n` is positive, `curr_lat` is either within the range [-90, 90] adjusted by the sum of all "North" and "South" movements divided by 111.195, or it is outside this range if the program terminated, indicating an invalid movement.
    print('YES' if curr_lat == 90 else 'NO')
#Overall this is what the function does:The function simulates a journey consisting of a series of parts with specified times and directions. It accepts input from the user, including the number of parts in the journey and the time and direction for each part. The function calculates the final latitude after all parts of the journey, assuming a starting latitude of 90 degrees North and using an approximation of 111.195 kilometers per degree of latitude. The function checks for and handles invalid movements, including those that would result in a latitude outside the range of -90 to 90 degrees or those that involve moving away from the pole when already at it. At the conclusion of the function, it prints 'YES' if the final latitude is 90 degrees North and 'NO' otherwise, effectively determining whether the journey ends back at the starting point. The function does not account for east or west movements in its calculations, effectively ignoring them. Potential edge cases include a journey with zero parts, journeys with times or directions that are not positive integers or one of the four cardinal directions, and journeys involving invalid movements that trigger the function to exit and print 'NO' before completing all parts.

