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
        
    #State: Output State: `t` is an integer such that 1 <= t <= 1440, `day` could be either 'AM' or 'PM', `n` is an input integer after all iterations of the loop.
    #
    #Explanation: The loop processes `n` time inputs in the format `h:m`, adjusting the hour based on whether it's AM or PM, and then prints the adjusted time along with the corresponding AM/PM designation. The initial value of `t` and `day` remain unchanged as they are not affected by the loop. After the loop completes, `day` will reflect the final AM/PM designation from one of the processed times, and `n` will be the number of iterations completed, which is an input integer.
#Overall this is what the function does:The function processes `n` time inputs in the format `h:m`, converting them to a 12-hour clock format with AM/PM designations. It prints each adjusted time. After processing, the function does not return any value but modifies the `day` variable to reflect the final AM/PM designation from one of the processed times and retains the input integer `n` as the number of iterations completed.

