#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440. Each of the following t lines contains a string s of length 5 in the format "hh:mm" where "hh" is a valid hour in 24-hour format (00 to 23) and "mm" is a valid minute in 24-hour format (00 to 59).
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
        
    #State: The loop will print `n` lines, each in the format "hh:mm AM" or "hh:mm PM", corresponding to the converted 12-hour format of the input times. The variables `t`, `day`, and `n` remain unchanged.
#Overall this is what the function does:The function reads an integer `n` representing the number of time entries, followed by `n` lines of strings each in the format "hh:mm" representing valid times in 24-hour format. It then prints each time converted to 12-hour format with an appropriate AM or PM suffix.

