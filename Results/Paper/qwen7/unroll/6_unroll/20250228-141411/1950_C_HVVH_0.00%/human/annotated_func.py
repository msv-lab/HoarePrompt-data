#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in the 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
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
        
    #State: day is 'AM' or 'PM', n is 0, h is 00, m is 00.
#Overall this is what the function does:The function processes a series of time inputs in the format "hh:mm" and converts them to a 12-hour clock format with AM/PM indicators. It prints each converted time. After processing all inputs, the final state includes `day` set to either 'AM' or 'PM', `n` set to 0, and `h` and `m` both set to 00.

