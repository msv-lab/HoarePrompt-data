#State of the program right berfore the function call: The function has access to the input data, which is an integer n representing the number of parts in the journey and n pairs of values, where each pair consists of a non-negative integer t_i representing the distance to be traveled and a string dir_i representing the direction, which can be "North", "South", "West", or "East".
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `t` and `dir` are the last input values if the loop executed, `position` is between -n*max(t) and 20000 + n*max(t) if all movements were valid and did not exceed boundaries or is 0 if the loop did not execute, and `valid` is False if any movement or condition made it so, otherwise True.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: `n` is a non-negative integer, `t` and `dir` are the last input values if the loop executed, `position` is between -n*max(t) and 20000 + n*max(t) if all movements were valid and did not exceed boundaries or is 0 if the loop did not execute. If `position` is not 0, then `valid` is `False`. If `position` is 0, the state of `valid` remains unchanged as there is no else part to alter it.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is a non-negative integer, `t` and `dir` are the last input values if the loop executed, `position` is between -n*max(t) and 20000 + n*max(t) if all movements were valid and did not exceed boundaries or is 0 if the loop did not execute. If `position` is not 0, then `valid` is `False`. If `position` is 0, then 'YES' has been printed to the console and `valid` is `True`, otherwise 'NO' has been printed to the console and `valid` remains `False`.
#Overall this is what the function does:The function determines whether a journey, defined by a sequence of steps with given distances and directions, ends at the starting point without exceeding certain boundaries or violating specific conditions. It accepts the number of steps and then the distance and direction for each step, validating the inputs and updating the position accordingly. The function checks for boundary conditions (position between 0 and 20000) and direction constraints (not moving West or East when at the boundary positions 0 or 20000). It returns 'YES' if the journey is valid and ends at the starting point, indicating that all steps were successfully processed without any violations, and 'NO' otherwise, indicating that at least one condition was not met. The function handles edge cases such as negative positions, exceeding the maximum position of 20000, moving West or East from boundary positions, and journey paths that do not return to the origin, adjusting the validation flag 'valid' based on these conditions. After execution, the program's state reflects the outcome of the journey validation, with 'YES' or 'NO' printed to the console and the 'valid' flag set accordingly. The final state does not modify the input data but rather evaluates the journey based on the provided steps, giving a clear indication of whether the journey adheres to the predefined rules and constraints.

