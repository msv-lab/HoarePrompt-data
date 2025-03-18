#State of the program right berfore the function call: The function should take a string s of length 5 with format hh:mm representing a valid time in the 24-hour format as input. The hour (hh) ranges from 00 to 23, and the minute (mm) ranges from 00 to 59. The input will always be a valid time in 24-hour format.
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
        
    #State: The loop will print the time in 12-hour format followed by 'AM' or 'PM' for each iteration, based on the input time and the value of `n`. The variables `h`, `m`, and `day` will be updated in each iteration, but the initial input string `s` and the integer `n` will remain unchanged.
#Overall this is what the function does:The function does not accept any parameters and does not return any values. Instead, it reads an integer `n` from the user input, which represents the number of time conversions to perform. For each of the `n` iterations, it reads a time in 24-hour format (hh:mm) from the user input, converts it to 12-hour format, and prints the converted time followed by 'AM' or 'PM'. The function does not modify any external state or variables, and it only affects the local variables `h`, `m`, and `day` within each iteration.

