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
        
    #State: Output State: t is an integer such that 1 <= t <= 1440, and for each test case, s is a string of length 6 (including the AM/PM indicator) representing the formatted time in the 12-hour format based on the original input time in the 24-hour format. The first two characters of s represent the hour in the 12-hour format, followed by ":", then the original minutes from the input time, and finally either "AM" or "PM" depending on whether the original hour was 12 or greater than 12.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` and a string `s` representing a time in the 24-hour format. For each test case, it converts the time from the 24-hour format to the 12-hour format and prints the formatted time along with "AM" or "PM". After processing all test cases, the function does not return any value; instead, it outputs the formatted times for each test case.

