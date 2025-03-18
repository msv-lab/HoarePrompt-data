#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 50, and for each of the n parts, t_i is a positive integer such that 1 <= t_i <= 10^6 and dir_i is one of the strings "North", "South", "West", or "East".
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 50; `position` is a value between 0 and 20000; `valid` is a boolean indicating whether all movements were valid based on the conditions within the loop; `t` is the last integer input received, and `dir` is the last directional input received. If at any point `position` went below 0 or above 20000, or if any invalid movement was attempted, `valid` will be False; otherwise, it remains True. If the loop does not execute, `position` remains 0 and `valid` is True.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: *`n` is a positive integer between 1 and 50; `position` is a value between 1 and 20000; `valid` is False; `t` is the last integer input received; `dir` is the last directional input received; if `position` is not 0, it indicates that some movements occurred leading to the current value of `position`, and `valid` reflects whether all these movements were valid. If the loop does not execute, `position` remains 0 and `valid` is True.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is a positive integer between 1 and 50; `position` is a value between 1 and 20000. If `valid` is True, then `position` reflects the outcome of valid movements, and `t` and `dir` remain unchanged. If `position` is 0, the output is 'NO', while `valid` remains True, indicating that no invalid movements occurred.
#Overall this is what the function does:The function reads a number of directional movements and calculates a final position based on these movements. It validates that the movements do not exceed certain bounds (0 to 20000) and checks if the final position is zero after all movements. If all movements are valid and the final position is 0, it prints 'YES'; otherwise, it prints 'NO'. The function does not accept parameters and expects user input for the number of movements and their details. It also checks for invalid movements, such as moving beyond the specified limits or attempting to move West or East when at the edges of the valid range.

