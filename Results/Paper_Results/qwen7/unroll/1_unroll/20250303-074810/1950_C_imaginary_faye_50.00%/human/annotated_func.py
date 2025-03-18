#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in the 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
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
        
    #State: Output State: The output state will consist of multiple lines, each line containing a transformed time string based on the input time string. For each input time "hh:mm", the code converts it to a 12-hour format with AM/PM notation and outputs it. If the input hour is '00', it is converted to '12'. Hours from '01' to '12' remain the same. Hours from '13' to '23' are converted by subtracting 12 and prefixing with '0'. The AM/PM indicator is determined by whether the hour is greater than or equal to '12'. Each line will also include either 'AM' or 'PM' based on the converted hour.
#Overall this is what the function does:The function processes a series of time strings formatted as "hh:mm" and converts them into a 12-hour format with AM/PM notation. For each input time, it prints the converted time string. If the input hour is '00', it is displayed as '12'. Hours from '01' to '12' remain unchanged. Hours from '13' to '23' are adjusted by subtracting 12 and prefixed with '0'. Additionally, it appends 'AM' or 'PM' based on whether the hour is greater than or equal to '12'. The function does not return any value; its primary action is to output the transformed time strings.

