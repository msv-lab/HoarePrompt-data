#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each of the t test cases, there is a string s of length 5 representing a valid time in 24-hour format where the first two characters represent the hour (hh) from 00 to 23 and the last two characters after the colon represent the minute (mm) from 00 to 59.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1440, `s` is a string of length 5 representing a valid time in 24-hour format, `n` is 0, `h` and `m` are the hour and minute of the last time processed, and `day` is either 'AM' or 'PM' based on the last time processed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a time in 24-hour format. It then converts this time to 12-hour format with AM/PM notation and prints the converted time.

