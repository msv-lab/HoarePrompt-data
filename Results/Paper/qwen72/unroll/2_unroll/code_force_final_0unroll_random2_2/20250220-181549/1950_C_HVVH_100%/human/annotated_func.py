#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and s is a string of length 5 in the format "hh:mm" where hh is an integer from 00 to 23 and mm is an integer from 00 to 59, representing a valid time in 24-hour format.
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
        
    #State: The values of `t`, `s`, and `n` remain unchanged. The value of `day` will be 'AM' or 'PM' depending on the last time input in the loop. The loop will print the time in 12-hour format followed by 'AM' or 'PM' for each iteration.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `n` from the user input, representing the number of time entries. For each of the `n` entries, it reads a time in the format "hh:mm" from the user input, converts it to a 12-hour format, and appends 'AM' or 'PM' based on the hour. The function prints each converted time followed by 'AM' or 'PM'. After the function concludes, the values of `t`, `s`, and `n` remain unchanged, and the value of `day` will be 'AM' or 'PM' depending on the last time input in the loop.

