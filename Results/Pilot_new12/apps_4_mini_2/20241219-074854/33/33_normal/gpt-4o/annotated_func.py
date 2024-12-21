#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 50, and for each i-th instruction, t_i is an integer (1 <= t_i <= 10^6) and dir_i is a string that can be "North", "South", "West", or "East".
def func():
    n = int(input())
    position = 0
    valid = True
    for _ in range(n):
        t, dir = input().split()
        
        t = int(t)
        
        if dir == 'North':
            if position - t < 0:
                valid = False
            position -= t
        elif dir == 'South':
            if position + t > 20000:
                valid = False
            position += t
        elif dir in ('West', 'East'):
            if position == 0 or position == 20000:
                valid = False
        
        if position < 0 or position > 20000:
            valid = False
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 50; `t_i` is a list of integers with 1 <= `t_i` <= 10^6; `position` is between 0 and 20000 inclusive; `valid` is a boolean that indicates whether all movements were valid based on the defined conditions.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 <= `n` <= 50; `t_i` is a list of integers with 1 <= `t_i` <= 10^6; `position` is between 0 and 20000 inclusive. If `position` is not equal to 0, `valid` is set to False, indicating that not all movements were valid based on the defined conditions.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 <= `n` <= 50; `t_i` is a list of integers with 1 <= `t_i` <= 10^6; `position` is between 0 and 20000 inclusive. If `valid` is True, 'YES' is printed. Otherwise, `valid` is set to False, indicating that not all movements were valid based on the defined conditions.
#Overall this is what the function does:The function reads a series of movement commands defined by a number of instructions, where each instruction consists of a distance and a direction. It validates each movement based on defined constraints such as not allowing the position to fall below 0 or exceed 20000, and also restricts certain movements when at boundaries (0 or 20000). At the end of the command series, if the final position is 0 and all movements were valid, it prints 'YES'; otherwise, it prints 'NO'. It ensures that the movements comply with the constraints throughout the execution, but it does not track or return the final Cartesian coordinates, just a validity message. Also, there is no handling for invalid input directions, meaning if an unsupported direction is provided, the function does not explicitly handle that case.

