#State of the program right berfore the function call: time_str is a string of length 5 in the format "hh:mm" where hh is an integer from 00 to 23 and mm is an integer from 00 to 59.
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
        
    #State: The output state is a series of strings, each representing a time in the format "hh:mm AM" or "hh:mm PM" based on the input times. The variable `time_str` remains unchanged as it is not modified within the loop.
#Overall this is what the function does:The function `func_1` processes a series of time strings provided by the user in the format "hh:mm" (where `hh` is an integer from 00 to 23 and `mm` is an integer from 00 to 59). For each input time string, it converts the time to a 12-hour format and appends "AM" or "PM" based on the hour. The function does not return any value; instead, it prints the converted time strings directly to the console. The original input time strings are not modified or stored.

