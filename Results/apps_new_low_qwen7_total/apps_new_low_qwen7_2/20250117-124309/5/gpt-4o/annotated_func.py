#State of the program right berfore the function call: h is an integer representing hours (00 to 23), m is an integer representing minutes (00 to 59), and x is an integer representing the snooze interval (1 to 60).
def func_1(h, m):
    """Check if the time h:m contains a '7'."""
    return '7' in str(h) or '7' in str(m)
    #The program returns True if either 'h' contains the digit 7 or 'm' contains the digit 7, otherwise it returns False
#Overall this is what the function does:The function `func_1` accepts two integers `h` and `m`, which represent hours (00 to 23) and minutes (00 to 59) respectively. It checks whether either `h` or `m` contains the digit 7. If either `h` or `m` contains the digit 7, the function returns `True`; otherwise, it returns `False`. There are no edge cases or missing functionality in the provided code since it correctly implements the described behavior.

#State of the program right berfore the function call: x is an integer between 1 and 60 inclusive, hh is an integer between 0 and 23 inclusive, and mm is an integer between 0 and 59 inclusive. The function func_1(hh, mm) returns True if the time represented by hh:mm contains the digit '7', and False otherwise.
def func_2():
    x = int(input())

hh, mm = map(int, input().split())

snooze_count = 0
    while not func_1(hh, mm):
        snooze_count += 1
        
        mm -= x
        
        if mm < 0:
            mm += 60
            hh -= 1
            if hh < 0:
                hh += 24
        
    #State of the program after the loop has been executed: `x` is an integer between 1 and 60, `hh` is an integer between 0 and 23, `mm` is an integer between 0 and 59, `snooze_count` is an integer greater than or equal to 0 and less than or equal to 1439 (since the maximum time in a day is 24 hours * 60 minutes = 1440 minutes).
    print(snooze_count)
#Overall this is what the function does:The function `func_2()` accepts two integer parameters `hh` and `mm`, representing hours and minutes respectively. It repeatedly decreases the minute value by `x` (an integer between 1 and 60) until the time `hh:mm` contains the digit '7'. For each iteration where the minute value decreases, the `snooze_count` is incremented. If the minute value becomes negative during the process, it wraps around to the next hour. Once the condition `func_1(hh, mm)` is met (i.e., the time contains the digit '7'), the function prints the total number of times the time was adjusted (`snooze_count`). The final state of the program includes updated values for `hh`, `mm`, and `snooze_count`. Potential edge cases include when `hh` or `mm` wrap around to the previous or next 24-hour cycle, respectively. The function does not return any value; instead, it outputs the `snooze_count` through the print statement.

