#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 50, and each of the next n lines contains an integer t_i (1 ≤ t_i ≤ 10^6) and a string dir_i that is one of "North", "South", "West", "East".
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 50; `position` is the final position after all movements, constrained between 0 and 20000; `valid` is True only if all movement conditions were satisfied during the loop execution; otherwise, `valid` is False. If `position` never goes below 0 or above 20000, then `valid` remains True; otherwise, it is set to False during the iterations. `t` is the last integer input processed, and `dir` is the last direction processed.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 50; `position` is the final position after all movements, constrained between 0 and 20000; `valid` is set to False since `position` is not equal to 0; `t` is the last integer input processed; `dir` is the last direction processed. If `position` were equal to 0, `valid` would remain True, but since it is not, `valid` is False after this check.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 50; `position` is the final position after all movements, constrained between 0 and 20000; if `valid` is True, 'YES' is printed. If `valid` is False (since `position` is not equal to 0), then 'NO' is printed and `valid` remains False.
#Overall this is what the function does:The function accepts a positive integer `n` followed by `n` pairs of integers and directions. It tracks a position that starts at 0 and can move based on the directions ("North", "South", "West", "East") with specified distances. If the movement would cause the position to go below 0 or above 20,000, or if the position is not back to 0 at the end, the function prints 'NO'; otherwise, it prints 'YES'. The function validates each move to ensure it remains within the constraints and checks the final position for validity.

