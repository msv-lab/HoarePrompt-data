#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each of the t test cases, there is a string s of length 5 with the format "hh:mm" where hh is a string representing the hour from "00" to "23" and mm is a string representing the minute from "00" to "59".
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
        
    #State: After processing `n` time strings, the output will display the last processed time in 12-hour format with the correct AM/PM designation. The variables `t` and the list of test cases remain unchanged.
#Overall this is what the function does:The function reads an integer `n` representing the number of time strings to process. For each of the `n` time strings in the format "hh:mm" (where "hh" is the hour from "00" to "23" and "mm" is the minute from "00" to "59"), it converts the time to a 12-hour format with the appropriate AM/PM designation and prints the result. The original input values remain unchanged.

