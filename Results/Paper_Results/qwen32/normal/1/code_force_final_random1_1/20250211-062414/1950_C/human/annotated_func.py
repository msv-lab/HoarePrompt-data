#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each of the t test cases, there is a string s of length 5 representing a valid time in 24-hour format where the first two characters represent the hour (hh) from 00 to 23 and the last two characters after the colon represent the minute (mm) from 00 to 59.
def func_1():
    for t in range(int(input())):
        s = input()
        
        h = s[:2]
        
        if h == '00':
            print('12', end='')
        elif int(h) <= 12:
            print(h, end='')
        else:
            print('0{}'.format(int(h) - 12), end='')
        
        print(s[2:], ['AM', 'PM'][int(h) >= 12])
        
    #State: The loop has completed processing all `t` test cases. The variables `s` and `h` hold the values from the last test case processed, but these are not retained outside the loop. The loop control variable `t` is now 0.
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases, then for each test case, it reads a string `s` of length 5 representing a time in 24-hour format. It converts this time into 12-hour format with AM/PM notation and prints the result. After processing all test cases, it terminates without returning any value.

