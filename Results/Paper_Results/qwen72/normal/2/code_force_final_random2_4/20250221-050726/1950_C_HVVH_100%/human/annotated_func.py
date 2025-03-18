#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and s is a string of length 5 in the format "hh:mm" where hh is an integer from 00 to 23 and mm is an integer from 00 to 59, representing a valid time in 24-hour format.
def func():
    day = 'AM'
    n = int(input())
    for _ in range(n):
        h, m = map(int, input().split(':'))
        
        if h == 0:
            h = 12
            day = 'AM'
        elif h > 12:
            h = h - 12
            day = 'PM'
        else:
            day = 'AM'
            if h == 12:
                day = 'PM'
        
        print(f'{h:02d}:{m:02d}', day)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1440, `s` is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format, `n` is the input integer (unchanged), `day` is either 'AM' or 'PM' based on the final value of `h` after all iterations, `h` is the last hour value processed, and `m` is the last minute value processed.
#Overall this is what the function does:The function reads an integer `n` from the user, then for each of the next `n` lines, it reads a time in the format "hh:mm". For each time, it converts the 24-hour format to a 12-hour format with AM/PM notation and prints the converted time. The function does not return any value. After the function concludes, `n` remains unchanged, and the last processed hour and minute values (`h` and `m`) and the corresponding AM/PM indicator (`day`) reflect the state of the last iteration.

