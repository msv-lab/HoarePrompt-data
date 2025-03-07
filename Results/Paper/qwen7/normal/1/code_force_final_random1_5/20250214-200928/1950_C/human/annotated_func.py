#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in the 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
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
        
    #State: t is the value of `int(input()) - 1`, `s` is the final input string, `h` is the first two characters of the final `s`.
#Overall this is what the function does:The function processes a series of time inputs in the format "hh:mm" and converts them to a 12-hour clock format, printing either "AM" or "PM" based on the hour. It iterates this process for a number of times specified by the user, where each iteration corresponds to one input. After processing all inputs, it does not return any value but prints the converted times directly.

