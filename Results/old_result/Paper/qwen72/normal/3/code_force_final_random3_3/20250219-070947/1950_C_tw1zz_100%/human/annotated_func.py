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
        
    #State: After the loop executes all the iterations, `t` is an integer such that 1 ≤ t ≤ 1440, `s` is a string of length 5 in the format "hh:mm", and the loop has printed the time in 12-hour format for each input string `s` provided by the user. For each input string, `h` is the hour part, `m` is the minute part, `h1` is the hour part converted to 12-hour format, and `time` is either 'AM' or 'PM' based on the hour part. The loop counter `_` has been incremented for each iteration, and the loop has executed `t` times.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the user, which represents the number of time conversion operations to perform. For each of the `t` operations, it reads a time string `s` in the format "hh:mm" from the user, where `hh` is the hour and `mm` is the minute. The function then converts the hour part of the time string to a 12-hour format and appends "AM" or "PM" accordingly. The converted time is printed in the format "hh:mm AM" or "hh:mm PM" for each input. After all iterations, the function has printed the converted times for `t` inputs, and the state of the program remains as it was before the function call, except for the output produced.

