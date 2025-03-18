#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and s is a string of length 5 in the format "hh:mm" where hh is an integer from 00 to 23 and mm is an integer from 00 to 59.
def func():
    for _ in range(int(input())):
        h, m = map(str, input().split(':'))
        
        h1, m1 = '', m
        
        time = ''
        
        if h == '01':
            h1 = '01'
            time = 'AM'
        elif h == '02':
            h1 = '02'
            time = 'AM'
        elif h == '03':
            h1 = '03'
            time = 'AM'
        elif h == '04':
            h1 = '04'
            time = 'AM'
        elif h == '05':
            h1 = '05'
            time = 'AM'
        elif h == '06':
            h1 = '06'
            time = 'AM'
        elif h == '07':
            h1 = '07'
            time = 'AM'
        elif h == '08':
            h1 = '08'
            time = 'AM'
        elif h == '09':
            h1 = '09'
            time = 'AM'
        elif h == '10':
            h1 = '10'
            time = 'AM'
        elif h == '11':
            h1 = '11'
            time = 'AM'
        elif h == '12':
            h1 = '12'
            time = 'PM'
        elif h == '13':
            h1 = '01'
            time = 'PM'
        elif h == '14':
            h1 = '02'
            time = 'PM'
        elif h == '15':
            h1 = '03'
            time = 'PM'
        elif h == '16':
            h1 = '04'
            time = 'PM'
        elif h == '17':
            h1 = '05'
            time = 'PM'
        elif h == '18':
            h1 = '06'
            time = 'PM'
        elif h == '19':
            h1 = '07'
            time = 'PM'
        elif h == '20':
            h1 = '08'
            time = 'PM'
        elif h == '21':
            h1 = '09'
            time = 'PM'
        elif h == '22':
            h1 = '10'
            time = 'PM'
        elif h == '23':
            h1 = '11'
            time = 'PM'
        elif h == '00':
            h1 = '12'
            time = 'AM'
        
        print(h1, ':', m, ' ', time, sep='')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1440, `s` is a string of length 5 in the format "hh:mm", `h` is the hour part of the input string provided by the user, `m` is the minute part of the input string provided by the user, `m1` is equal to `m`. For each valid input hour `h` (from '00' to '23'), `h1` is set to the corresponding hour in 12-hour format, and `time` is set to 'AM' or 'PM' based on the hour. If `h` is not a valid hour, `h1` remains an empty string and `time` remains an empty string.
#Overall this is what the function does:The function reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads a time string `s` in the format "hh:mm" from the user, where `hh` is the hour (from '00' to '23') and `mm` is the minute (from '00' to '59'). The function converts the hour part of the time string to a 12-hour format and determines whether it is 'AM' or 'PM'. It then prints the time in the format "hh:mm AM/PM" for each input time. The function does not return any value. After the function concludes, `t` remains an integer between 1 and 1440, and `s` is a string of length 5 in the format "hh:mm". The variables `h`, `m`, `h1`, and `time` are used internally and are not retained after the function execution.

