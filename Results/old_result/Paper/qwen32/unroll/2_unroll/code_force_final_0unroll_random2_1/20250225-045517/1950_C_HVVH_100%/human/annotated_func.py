#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each of the t test cases, the input is a string s of length 5 in the format "hh:mm" where hh is a two-digit integer representing hours from 00 to 23, and mm is a two-digit integer representing minutes from 00 to 59.
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
        
    #State: `t` is an integer such that 1 <= t <= 1440, `day` is the last determined day ('AM' or 'PM') based on the last input time, and `n` is the input integer.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases, and for each test case, it reads a time in the format "hh:mm". It then converts this time from 24-hour format to 12-hour format with AM/PM designation and prints the result.

