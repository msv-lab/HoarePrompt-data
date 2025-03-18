#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440. Each of the following t lines contains a string s of length 5 in the format "hh:mm" where hh is a two-digit string representing the hour from "00" to "23" and mm is a two-digit string representing the minute from "00" to "59". The input will always be a valid time in 24-hour format.
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
        
    #State: Each of the t lines contains a string in the format "hh:mm AM" or "hh:mm PM" representing the corresponding input time in 12-hour format with AM/PM notation.
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of time entries, followed by `t` lines of strings in the format "hh:mm" representing times in 24-hour format. It then prints each time converted to 12-hour format with AM/PM notation.

