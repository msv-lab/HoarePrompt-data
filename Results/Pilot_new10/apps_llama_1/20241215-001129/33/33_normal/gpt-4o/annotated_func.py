#State of the program right berfore the function call: The input consists of n, the number of journey parts, followed by n lines, each containing a distance t_i and a direction dir_i, where 1 ≤ n ≤ 50, 1 ≤ t_i ≤ 10^6, and dir_i is one of "North", "South", "West", or "East".
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 50 (inclusive), `position` is an integer between 0 and 20000 (inclusive) or out of bounds based on the user inputs, and `valid` is `True` if all movements were within bounds and did not attempt 'West' or 'East' at boundary positions, otherwise `False`.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: `n` is a positive integer between 1 and 50 (inclusive), if `position` is not equal to 0, then `position` is an integer between 1 and 20000 (inclusive) and `valid` is `False`; otherwise, the state of `position` and `valid` remains as defined by the precondition, with `position` being 0.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is a positive integer between 1 and 50 (inclusive), `position` is 0, and if `valid` is `True`, then 'YES' has been printed, otherwise 'NO' has been printed to the console and `valid` is `False`.
#Overall this is what the function does:The function processes a series of movements defined by distance and direction, checks the validity of these movements based on given constraints (bounds and direction at boundary positions), and prints "YES" if all movements are valid and end at the starting position; otherwise, it prints "NO", covering all potential cases including invalid inputs and edge scenarios not explicitly handled by the function's logic.

