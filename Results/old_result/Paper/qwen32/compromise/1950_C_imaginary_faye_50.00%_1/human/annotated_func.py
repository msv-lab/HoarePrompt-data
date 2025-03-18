#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each of the t test cases, there is a string s of length 5 in the format "hh:mm" where hh is a two-digit string representing the hour from 00 to 23 and mm is a two-digit string representing the minute from 00 to 59.
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
        
    #State: For each of the t test cases, the output will be a string in the format "hh:mm [AM/PM]", where "hh" is the hour converted to a 12-hour format, "mm" remains the same, and "[AM/PM]" indicates whether the time is in the AM or PM period.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a time string `s` in the format "hh:mm". It then converts the time to a 12-hour format with AM/PM notation and prints the result.

