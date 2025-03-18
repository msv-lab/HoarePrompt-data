#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1440, and s is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format, where hh is an integer from 00 to 23 and mm is an integer from 00 to 59.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 1440, `s` is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format, `n` is 0, `h` and `m` are integers representing the hour and minute from the input string respectively. For each iteration, if `h` is 0, `h` is updated to 12 and `day` is 'AM'. If `h` is greater than 12, `h` is updated to `h - 12` and `day` is 'PM'. If `h` is 12, `day` is 'PM'. Otherwise, `day` remains 'AM'.
#Overall this is what the function does:The function reads an integer `n` indicating the number of time conversions to perform. For each conversion, it reads a time in the format "hh:mm" and converts it to a 12-hour format with AM/PM notation, printing the converted time. The function does not return any value; its primary action is to print the converted times. After the function concludes, `n` is 0, and the input times have been processed and printed in the 12-hour format with AM/PM notation.

