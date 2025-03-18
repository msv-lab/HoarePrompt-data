#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each of the t test cases, there is a string s of length 5 representing a valid time in 24-hour format, where the first two characters hh represent the hour from 00 to 23, and the last two characters mm represent the minute from 00 to 59.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1440, and for each of the t test cases, there is a string `s` of length 5 representing a valid time in 24-hour format, where the first two characters `hh` represent the hour from 00 to 23, and the last two characters `mm` represent the minute from 00 to 59; `day` is `'AM'`; `n` is an input integer.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases, and for each test case, it reads a time in 24-hour format (hh:mm). It then converts each time to 12-hour format with AM/PM notation and prints the result.

