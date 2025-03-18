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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 1440, `day` is either 'AM' or 'PM' based on the last time conversion in the loop, `n` is the number of times the loop has executed.
    #
    #Explanation: The loop processes a series of time inputs and adjusts them to a 12-hour format with AM/PM notation. After all iterations, the final value of `day` will be determined by the last time conversion operation performed, and `n` will be the total number of times the loop has run. The value of `t` remains unchanged unless it is modified within the loop, which it is not in this case.
#Overall this is what the function does:The function processes a series of time inputs in 24-hour format and converts them to 12-hour format with AM/PM notation. It prints each converted time and the corresponding AM/PM designation. The function does not return any value but modifies the `day` variable to reflect the last conversion performed. The variable `n` keeps track of the number of time conversions executed.

