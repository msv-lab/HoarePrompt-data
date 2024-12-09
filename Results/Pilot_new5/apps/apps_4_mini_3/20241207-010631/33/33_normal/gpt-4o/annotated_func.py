#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 50, and for each of the next n lines, t_i is a positive integer such that 1 ≤ t_i ≤ 10^6 and dir_i is one of the strings "North", "South", "West", or "East".
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 50. `position` is within the range [0, 20000] after all iterations, and `valid` indicates whether all movements were valid according to the conditions specified in the loop. If any movement caused `position` to go out of bounds or violated any conditions, `valid` will be False; otherwise, it will remain True.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 50. If `position` is not equal to 0, then `valid` is False, indicating that at least one movement was invalid; otherwise, `position` remains within the range [0, 20000] and `valid` indicates that all movements were valid.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 50. If `valid` is True, then `position` is within the range [0, 20000], and the output printed is 'YES', indicating that all movements were valid. If `valid` is False, `position` remains within the range [0, 20000], indicating that at least one movement was invalid.
#Overall this is what the function does:The function accepts a positive integer `n` which indicates how many movements to process. For each movement, it takes a positive integer `t` and a direction (`North`, `South`, `East`, or `West`). The function checks if these movements keep the position within the bounds of 0 to 20000. If any movement causes the position to go below 0 or above 20000, or if the final position is not 0, the function prints 'NO'. Otherwise, it prints 'YES'. The function does not return a typical value, but rather prints the result based on the validity of the movements.

