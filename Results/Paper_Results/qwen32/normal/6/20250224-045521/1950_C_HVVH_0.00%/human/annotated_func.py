#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each of the t test cases, the input is a string s of length 5 with the format "hh:mm" where hh is an integer from 00 to 23 and mm is an integer from 00 to 59, representing a valid time in the 24-hour format.
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
        
    #State: `t` is an integer such that 1 <= t <= 1440, `s` is a string of length 5 with the format "hh:mm", `n` is 0, `m` is the minute part of the input time, and `h` and `day` are determined based on the value of `h` for the last input time. If `h` is 0, `h` is set to 12 and `day` is 'AM'. If `h` is greater than 12, `h` is reduced by 12 and `day` is 'PM'. If `h` is 12, `day` remains 'PM'. If `h` is less than 12, `day` remains 'PM' unless `h` is 0, in which case `day` is set to 'AM'.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a time in 24-hour format "hh:mm", converts it to 12-hour format with AM/PM, and prints the converted time.

