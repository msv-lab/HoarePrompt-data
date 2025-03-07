#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
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
        
    #State: Output State: The output state will consist of multiple lines, each containing a transformed time string based on the input time. For each input time `s` in the format "hh:mm", the code converts it to a 12-hour format with AM/PM notation and outputs it. If the hour is '00', it prints '12'. If the hour is between '01' and '12', it prints the hour as is. If the hour is between '13' and '23', it subtracts 12 from the hour and adds a leading zero. The output also appends either 'AM' or 'PM' based on whether the hour is 12 or greater than '12'.
#Overall this is what the function does:The function processes an integer `t` (representing minutes since midnight) and a string `s` in the format "hh:mm". It converts the time string `s` to a 12-hour format with AM/PM notation and outputs it. If the hour is '00', it prints '12'. If the hour is between '01' and '12', it prints the hour as is. If the hour is between '13' and '23', it subtracts 12 from the hour and adds a leading zero. The output also appends either 'AM' or 'PM' based on whether the hour is 12 or greater than '12'. The function does not return any value; it only prints the converted time strings.

