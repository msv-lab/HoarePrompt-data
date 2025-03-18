#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and s is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format, where hh is an integer from 00 to 23 and mm is an integer from 00 to 59.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1440, `s` is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format, `n` is 0, `day` is either 'AM' or 'PM' based on the initial conditions and the input times provided. For each iteration, if `h` is 0, `h` is set to 12 and `day` is 'AM'. If `h` > 12, `h` is decreased by 12 and `day` is 'PM'. If `h` is 12, `day` is 'AM'. Otherwise, `day` remains 'PM'.
#Overall this is what the function does:The function reads an integer `n` from the user, representing the number of times it will process a time input. For each of the `n` times, it reads a time in the format "hh:mm" from the user, converts it to a 12-hour format, and prints the time along with 'AM' or 'PM' based on the hour. The function does not return any value. After the function concludes, `n` is 0, and the program state is such that the function has printed the converted times for all `n` inputs.

