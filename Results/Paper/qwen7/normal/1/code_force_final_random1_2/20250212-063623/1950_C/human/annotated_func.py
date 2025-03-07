#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 1440, s is an input string representing a valid time in the format "hh:mm", and h is the first two characters of s. If h is '00', no changes are made to t and h. If h is not '00', no changes are made to t and h after the loop completes.
#Overall this is what the function does:The function processes a series of times in the format "hh:mm" and converts them to a 12-hour clock format, printing whether the time is AM or PM. It does not return any value but prints the converted times. The function iterates over the number of test cases specified by the user, converting each time and printing the result. If the hour part of the time is '00', it prints '12' instead. For hours 01 to 12, it prints the hour as is. For hours 13 to 23, it prints the hour minus 12 with a leading zero.

