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
            day = 'AM'
            if h == 12:
                day = 'PM'
        
        print(f'{h:02d}:{m:02d}', day)
        
    #State: Output State: After the loop executes all its iterations, `day` will be either 'AM' or 'PM', depending on the final value of `h` as processed by the loop. The variable `n` will be set to 0 because the loop runs from `range(n)`, and once all iterations are completed, `n` will no longer be greater than 0. The variable `h` will be an integer within the range of 1 to 23, with values originally greater than 12 being adjusted to `h - 12`. The variable `m` will retain its original input integer value, as it is not modified by the loop.
    #
    #In summary, `n` will be 0, `day` will be either 'AM' or 'PM' based on the final value of `h`, `h` will be an integer between 1 and 23 (with values greater than 12 adjusted), and `m` will be the same as the initial input integer.
#Overall this is what the function does:The function processes a series of times in the format "hh:mm" and converts them to 12-hour format with AM/PM notation. It prints each converted time and the corresponding AM/PM designation. After processing all inputs, it sets the counter `n` to 0 and updates the `day` variable to either 'AM' or 'PM' based on the final hour value. The function does not return any value but modifies the `day` and `n` variables and prints the converted times.

