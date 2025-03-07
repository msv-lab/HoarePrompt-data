#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440. Each of the t test cases is a string s of length 5 with the format "hh:mm", where "hh" is a valid hour in 24-hour format (00 to 23) and "mm" is a valid minute (00 to 59).
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
        
    #State: t is an integer such that 1 <= t <= 1440; Each of the t test cases is a string s of length 5 with the format "hh:mm", where "hh" is a valid hour in 24-hour format (00 to 23) and "mm" is a valid minute (00 to 59); day is 'AM'; n is an input integer.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases, and for each test case, it reads a time in 24-hour format "hh:mm". It then converts this time to 12-hour format with an AM/PM suffix and prints the result.

