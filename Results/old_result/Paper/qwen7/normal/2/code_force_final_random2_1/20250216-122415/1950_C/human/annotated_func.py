#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
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
        
    #State: After the loop executes all its iterations, `t` is an integer such that 1 ≤ t ≤ 1440, `day` is either 'AM' or 'PM', `n` is the original input integer minus the number of iterations the loop executed, `h` is the integer part of the final input split by `:`, and `m` is the integer part of the final input split by `:`. If `h` is 0, `day` is set to 'AM' and `h` is set to 12. Otherwise, if `h` is greater than 12, then `day` is set to 'PM' and `h` is adjusted to `h - 12`. If `h` is 12 or less, then `day` remains unchanged.
#Overall this is what the function does:The function processes a series of times in the format "hh:mm" and prints them in 12-hour format along with AM/PM. It does not return any value.

