#State of the program right berfore the function call: Input is a sequence of n pairs of values where n is a positive integer, each pair consisting of a non-negative integer t representing the length of a journey in kilometers (1 ≤ t ≤ 10^6), and a string dir representing the direction of the journey, which can be one of "North", "South", "West", or "East".
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `t` and `dir` are the last input values, `position` is the final position after all movements within the bounds 0 to 20000, and `valid` is `True` if all movements were valid, `False` otherwise.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: *`n` is a positive integer, `t` and `dir` are the last input values, `position` is the final position after all movements within the bounds 0 to 20000. If `position` is not equal to 0, `valid` is `False`. If `position` is 0, the state of `valid` is unchanged, as there is no else part to modify it.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is a positive integer, `t` and `dir` are the last input values, `position` is the final position after all movements within the bounds 0 to 20000. If `position` is 0, `valid` is `True`. If `position` is not 0, `valid` is `False` and 'NO' has been printed to the console.
#Overall this is what the function does:The function accepts a sequence of pairs of values representing journeys, where each pair consists of a non-negative integer for the journey length and a string for the direction, which can be "North", "South", "West", or "East". It processes this information to determine if a series of movements, where each movement is within the bounds of 0 to 20000, results in a final position of 0 and if all movements are valid according to the given rules. The function prints 'YES' to the console if the final position is 0 and all movements are valid; otherwise, it prints 'NO'. The function considers the following edge cases: it checks for valid directions, ensures that movements do not exceed the bounds of 0 to 20000, and verifies that movements in "West" or "East" directions do not occur when the position is 0 or 20000. The final state of the program includes the console output ('YES' or 'NO') based on the validity of the movements and the final position.

