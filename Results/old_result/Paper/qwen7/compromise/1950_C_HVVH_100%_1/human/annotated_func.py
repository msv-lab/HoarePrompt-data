#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in the 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
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
        
    #State: Output State: `t` is an integer such that 1 <= t <= 1440, `day` is either 'AM' or 'PM' based on the last time conversion in the loop, `n` is the number of times the loop has executed. After executing all the iterations of the loop, `t` remains unchanged, `day` will be 'AM' or 'PM' depending on the last time conversion performed in the loop, and `n` is equal to the number of times the loop has run.
#Overall this is what the function does:The function processes a series of times provided as input, converting them to a 12-hour format with AM/PM notation. It prints each converted time and updates the AM/PM indicator accordingly. After processing all inputs, it outputs the final AM/PM indicator but leaves the original integer `t` unchanged.

