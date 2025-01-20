#State of the program right berfore the function call: h and m are integers representing hours and minutes respectively, such that 0 <= h <= 23 and 0 <= m <= 59. The function checks if the time h:m contains the digit '7'.
def func_1(h, m):
    """Check if the time h:m contains a '7'."""
    return '7' in str(h) or '7' in str(m)
    #The program returns True if either the hour 'h' or the minute 'm' contains the digit '7', otherwise it returns False
#Overall this is what the function does:The function `func_1` accepts two parameters `h` and `m`, which represent hours and minutes respectively, with constraints 0 ≤ h ≤ 23 and 0 ≤ m ≤ 59. It checks whether either the hour `h` or the minute `m` contains the digit '7'. If either `h` or `m` contains the digit '7', the function returns `True`. Otherwise, it returns `False`. There are no specific edge cases mentioned in the code or annotations, but the function correctly handles valid inputs within the specified range.

#State of the program right berfore the function call: x is an integer such that 1 ≤ x ≤ 60, hh and mm are integers representing hours and minutes respectively where 00 ≤ hh ≤ 23 and 00 ≤ mm ≤ 59, and func_1(hh, mm) is a boolean function that returns True if the time represented by hh:mm contains the digit '7' and False otherwise.
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
        
    #State of the program after the loop has been executed: snooze_count is the number of iterations the loop executed, mm is (60 * snooze_count) - x, and hh is adjusted to be within the range [0, 23] based on the value of mm.
    print(snooze_count)
#Overall this is what the function does:The function `func_2` simulates a countdown timer that starts from the given time `hh:mm` and decrements the minutes by `x` until the time contains the digit '7' according to the function `func_1`. It keeps track of the number of times the timer decrements (`snooze_count`). If the minutes go below zero, it wraps around to the next hour. After the loop ends, it prints the number of times the timer was decremented.

