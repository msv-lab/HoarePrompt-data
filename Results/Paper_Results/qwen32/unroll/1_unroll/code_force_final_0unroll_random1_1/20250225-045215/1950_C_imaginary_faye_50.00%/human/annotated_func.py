#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each test case, the input is a string s of length 5 representing a valid time in 24-hour format, where the first two characters (hh) represent the hour from 00 to 23 and the last two characters (mm) represent the minutes from 00 to 59.
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
        
    #State: The output state consists of the printed times in 12-hour format with AM/PM suffix for each of the t test cases. The variables t, s, and h do not retain any specific values after the loop finishes.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string `s` of length 5 representing a valid time in 24-hour format. It then prints the time converted to 12-hour format with an "AM" or "PM" suffix accordingly.

