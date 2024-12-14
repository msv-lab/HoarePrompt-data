#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 50), and for each part of the journey, t_i is a positive integer (1 ≤ t_i ≤ 10^6) representing the distance, and dir_i is a string that is either "North", "South", "West", or "East".
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 50), `position` is within the range [0, 20000], `valid` is dependent on whether all moves were valid during iterations, and `t` remains an integer input value from the iterations.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 50) and `position` is within the range [0, 20000]. If `position` is not equal to 0, then `valid` is False and `t` remains an integer input value from the iterations.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is a positive integer (1 ≤ n ≤ 50), `position` is within the range [0, 20000]. If `valid` is True and `position` is not equal to 0, then the output is 'YES'; if `valid` is False, then 'NO' is printed regardless of the state of `position`.
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 50) that indicates the number of movements, and for each movement, it takes a positive integer `t` representing the distance and a direction `dir` which can be "North", "South", "West", or "East". The function checks whether each movement keeps the position within the valid range of 0 to 20000. It determines if the series of movements results in the final position being exactly 0, and returns 'YES' if all movements are valid and the final position is 0, or 'NO' otherwise. Additionally, the function considers invalid movements such as moving North beyond the starting point or moving South beyond 20000, and invalid directional movements when at the boundaries.

