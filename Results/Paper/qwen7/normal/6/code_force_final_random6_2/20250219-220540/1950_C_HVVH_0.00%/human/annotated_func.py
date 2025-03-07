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
            day = 'PM'
            if h == 12:
                day = 'AM'
        
        print(f'{h:02d}:{m:02d}', day)
        
    #State: Output State: The final output state after the loop executes all iterations will depend on the values of `h` and `m` provided in each iteration, as well as the initial value of `t`. Here's the breakdown:
    #
    #- `t` remains unchanged from the initial state since it is not affected by the loop.
    #- `day` will be determined by the last value of `h` processed in the loop according to the rules given:
    #  - If `h` is 0, `day` will be 'AM'.
    #  - If `h` is 12, `day` will be 'PM'.
    #  - Otherwise, `day` will be 'PM'.
    #- `h` and `m` will reflect the last values processed in the loop:
    #  - If `h` was 0 before the last conversion, it will be set to 12.
    #  - If `h` was greater than 12, it will be reduced by 12.
    #  - If `h` was 12, it will be reset to 0.
    #  - `m` will retain its original value from the last input.
    #
    #In summary, the output state will have `t` unchanged, `day` set based on the final `h` value, and `h` and `m` reflecting the last input values processed in the loop.
#Overall this is what the function does:The function processes a series of times in the format "hh:mm" and converts them to a 12-hour clock format, printing each converted time along with 'AM' or 'PM'. After processing all inputs, it prints the last converted time and the corresponding AM/PM indicator. The initial value of `t` remains unchanged throughout the function's execution.

