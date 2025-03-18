#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each of the t test cases, there is a string s of length 5 in the format "hh:mm" where hh is an integer from 00 to 23 and mm is an integer from 00 to 59, representing a valid time in 24-hour format.
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
        
    #State: The loop has executed `t` times, where `t` is the initial integer input representing the number of test cases. For each test case, a string `s` in the format "hh:mm" is processed. The first two characters `h` of `s` are converted to a 12-hour format, and "AM" or "PM" is appended based on whether the original hour is less than 12 or not. After all `t` iterations, all test cases have been processed and their corresponding outputs (in 12-hour format with AM/PM) have been printed.
#Overall this is what the function does:The function `func_1` processes `t` test cases, each consisting of a string `s` in the format "hh:mm" representing a valid time in 24-hour format. For each test case, it converts the time to a 12-hour format and appends "AM" or "PM" accordingly, then prints the result.

