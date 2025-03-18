#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each of the t test cases, there is a string s of length 5 with the format "hh:mm" where hh is a string representing the hour from "00" to "23" and mm is a string representing the minute from "00" to "59".
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
        
    #State: All test cases have been processed and printed in the required format. The variable `t` is 0, `s` holds the last input string, and `h` holds the hour part of the last input string.
#Overall this is what the function does:The function processes a specified number of time strings in the format "hh:mm" and prints each time converted to a 12-hour format with an AM/PM suffix.

