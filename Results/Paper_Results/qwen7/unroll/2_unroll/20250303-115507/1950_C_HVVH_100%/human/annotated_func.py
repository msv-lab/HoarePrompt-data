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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 1440, `day` is either 'AM' or 'PM' based on the last time conversion in the loop, `n` is the number of times the loop has executed.
    #
    #After the loop executes all the iterations, `t` remains unchanged as it is not affected by the loop. The `day` will be determined by the last time conversion operation inside the loop, which depends on the last input time (`h`, `m`). If the last `h` is 0, `day` will be 'AM'; if `h` is greater than 12, `day` will be 'PM'; otherwise, `day` will be 'AM'. The variable `n` will be equal to the number of times the loop has executed, which is provided as input.
#Overall this is what the function does:The function processes multiple time inputs in the format "hh:mm" and converts them to a 12-hour clock format with AM/PM notation. It prints each converted time. The function does not return any value but modifies the `day` variable to reflect the last converted time's AM/PM status and keeps track of the number of inputs processed through the `n` variable. The initial value of `t` remains unchanged as it is not used within the function.

