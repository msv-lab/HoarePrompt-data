#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each of the t test cases, there is a string s of length 5 in the format "hh:mm" where hh is a valid hour in 24-hour format (00 to 23) and mm is a valid minute (00 to 59).
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
        
    #State: t is an integer such that 1 <= t <= 1440, and for each of the t test cases, there is a string s of length 5 in the format "hh:mm" where hh is a valid hour in 24-hour format (00 to 23) and mm is a valid minute (00 to 59); day is 'AM'; n is an input integer.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases, followed by `n` time strings in the format "hh:mm" in 24-hour format. For each time, it converts and prints the time in 12-hour format along with the appropriate AM or PM designation.

