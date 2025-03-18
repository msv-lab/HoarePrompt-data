#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each of the t test cases, there is a string s of length 5 representing a valid time in 24-hour format, where s is in the format "hh:mm" with hh ranging from "00" to "23" and mm ranging from "00" to "59".
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
        
    #State: `t` is an integer such that 1 <= t <= 1440, `s` is a string of length 5 representing a valid time in 24-hour format, `n` is 0, `m` is the input minute as an integer. If `h` was 0, then `h` is set to 12 and `day` is 'AM'. If `h` > 12, then `h` is the input hour minus 12 and `day` is 'PM'. If `h` == 12, `day` is 'AM'. Otherwise, `day` remains 'PM'.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases, where each test case is a time in 24-hour format "hh:mm". For each test case, it converts the time to 12-hour format with an AM/PM indicator and prints the result.

