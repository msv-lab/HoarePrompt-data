#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50. For each i from 1 to n, t_{i} is an integer such that 1 ≤ t_{i} ≤ 10^6, and dir_{i} is one of "North", "South", "West", "East".
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `position` is an integer between 0 and 20000 inclusive, `valid` is `True`, `t` is an integer such that 1 ≤ t ≤ 10^6, and `dir` is one of "North", "South", "West", "East"
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: *`n` is a non-negative integer, `position` is an integer between 0 and 20000 inclusive, `valid` is False, `t` is an integer such that 1 ≤ t ≤ 10^6, and `dir` is one of "North", "South", "West", "East". This is because if `position` is not equal to 0, then `valid` is set to False, regardless of the value of `n`. If `position` is 0, there is no change to the variables as there is no else part in the code.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is a non-negative integer, `position` is an integer between 0 and 20000 inclusive, `valid` is either True or False, `t` is an integer such that 1 ≤ t ≤ 10^6, and `dir` is one of "North", "South", "West", "East". If `valid` is True, the console prints 'YES'. If `valid` is False, the console prints 'NO'.
#Overall this is what the function does:The function processes a series of movements defined by distances `t_i` and directions (`North`, `South`, `West`, `East`) for `n` steps, where `1 ≤ n ≤ 50` and `1 ≤ t_i ≤ 10^6`. It checks if the final position of the movement sequence is exactly at position 0. If the final position is not 0, the function sets `valid` to `False`. The function then prints 'YES' if `valid` is `True` (indicating the final position is 0), and 'NO' otherwise. Edge cases include invalid movements (e.g., moving North when the position is already 0, moving South when the position is already 20000).

