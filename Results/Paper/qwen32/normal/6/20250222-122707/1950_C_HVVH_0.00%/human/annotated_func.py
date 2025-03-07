#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each of the t test cases, there is a string s of length 5 representing a valid time in 24-hour format (hh:mm) where 00 <= hh <= 23 and 00 <= mm <= 59.
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
        
    #State: `t` is an integer such that 1 <= t <= 1440, for each of the t test cases, there is a string `s` of length 5 representing a valid time in 24-hour format (hh:mm) where 00 <= hh <= 23 and 00 <= mm <= 59; `h` and `m` are the hour and minute values of the last processed time, adjusted to 12-hour format; `day` is 'AM' if the last processed time was originally 00:00 to 11:59 (except 00:00 which is 12:00 AM), and 'PM' if the last processed time was 12:00 to 23:59; `n` is 0.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases, and for each test case, it reads a time in 24-hour format (hh:mm). It then prints the equivalent time in 12-hour format (hh:mm) along with the appropriate AM/PM designation.

