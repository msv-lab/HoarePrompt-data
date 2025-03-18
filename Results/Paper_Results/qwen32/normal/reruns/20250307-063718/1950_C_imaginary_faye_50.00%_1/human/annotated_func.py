#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each test case, s is a string of length 5 in the format "hh:mm" where hh is a two-digit integer from "00" to "23" representing hours, and mm is a two-digit integer from "00" to "59" representing minutes.
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
        
    #State: After the loop executes all the iterations, `t` will be 0, and no further `s` or `h` will be processed. The loop will have printed the 12-hour format time with AM/PM for each of the initial `t` inputs.
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases and, for each test case, reads a string `s` in the format "hh:mm". It then prints the time in 12-hour format with AM/PM for each test case.

