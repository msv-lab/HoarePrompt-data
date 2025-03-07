#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and s is a string of length 5 in the format "hh:mm" where hh is an integer from 00 to 23 and mm is an integer from 00 to 59.
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
            day = 'PM'
            if h == 12:
                day = 'AM'
        
        print(f'{h:02d}:{m:02d}', day)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1440, `s` is a string of length 5 in the format "hh:mm" where hh is an integer from 00 to 23 and mm is an integer from 00 to 59, `n` is greater than or equal to 0, `_` is `n-1`, `h` and `m` are integers derived from the input string `s`. If `h` is 0, `h` is updated to 12 and `day` is set to 'AM'. If `h` > 12, `h` is updated to `h - 12` and `day` is set to 'PM'. If `h` is 12, `day` is set to 'AM'. Otherwise, `day` remains 'PM'.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, then for `n` times, it reads a time in the format "hh:mm" from the user, converts the 24-hour format to a 12-hour format, and prints the converted time along with the appropriate AM/PM indicator. The function does not return any value. After the function concludes, the program state is unchanged except for the printed output.

