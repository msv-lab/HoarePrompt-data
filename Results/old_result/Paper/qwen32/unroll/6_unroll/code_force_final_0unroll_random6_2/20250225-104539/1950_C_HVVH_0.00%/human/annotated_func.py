#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440. Each of the following t lines contains a string s of length 5 in the format "hh:mm", where hh is a two-digit integer from "00" to "23" representing the hour, and mm is a two-digit integer from "00" to "59" representing the minute. The input will always be a valid time in 24-hour format.
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
        
    #State: The output state consists of `n` lines, each representing a time in 12-hour format with AM/PM. Each line corresponds to the time converted from the 24-hour format given in the input. The variable `t` and the input times remain unchanged.
#Overall this is what the function does:The function reads an integer `n` representing the number of time entries, followed by `n` time strings in the format "hh:mm" in 24-hour format. It converts each time to the 12-hour format with AM/PM and prints the result. The original input values remain unchanged.

