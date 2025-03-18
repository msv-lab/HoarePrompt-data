#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and s is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format, where hh is an integer from 00 to 23 and mm is an integer from 00 to 59.
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
            time = 'AM'
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
            time = 'PM'
        
        print(h1, ':', m, ' ', time, sep='')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1440, `s` is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format. For each iteration, the hour part `h` and minute part `m` of the input time are processed. If `h` is between '01' and '12', `h1` is set to `h` and `time` is set to 'AM'. If `h` is between '13' and '23', `h1` is set to the corresponding 12-hour format hour (e.g., '13' becomes '01', '14' becomes '02', etc.) and `time` is set to 'PM'. If `h` is '00', `h1` is set to '12' and `time` is set to 'PM'. The minute part `m1` is always set to `m`. After all iterations, the loop has printed the converted 12-hour format time for each input time.
#Overall this is what the function does:The function processes an integer `t` and a series of input times in 24-hour format "hh:mm". For each input time, it converts the hour part to a 12-hour format and appends 'AM' or 'PM' accordingly. The minute part remains unchanged. The function prints the converted 12-hour format time for each input time. The function does not return any value. After the function concludes, `t` is an integer such that 1 ≤ t ≤ 1440, and the input times have been converted and printed in 12-hour format.

