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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 1440, `day` is either 'AM' or 'PM', `n` is 0 (since it was decremented by 1 each iteration until it reached 0), `h` is an integer between 1 and 12, and `m` is an integer.
    #
    #In this final state, after all iterations of the loop have completed, `n` has been reduced to 0. The values of `t`, `day`, `h`, and `m` remain as they were last modified within the loop. `t` and `m` are unaffected by the loop since they are not used inside the loop, while `day` and `h` are adjusted based on the input provided during each iteration of the loop.
#Overall this is what the function does:The function processes a series of time inputs in the format "hh:mm", converting them to a 12-hour clock format with AM/PM notation. It prints each converted time and the corresponding AM/PM designation. After processing all inputs, it sets the loop counter `n` to 0 and leaves the initial values of `t`, `h`, and `m` unchanged, while updating `day` and `h` based on the input times.

