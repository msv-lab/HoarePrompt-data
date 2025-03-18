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
        
    #State: After all iterations of the loop, `t` is an integer such that 1 ≤ t ≤ 1440, `s` is a string of length 5 in the format "hh:mm". For each iteration, `h` is the hour part of the input string, `m` is the minute part of the input string, `m1` is equal to `m`, and `time` is either 'AM' or 'PM'. If `h` is '01' to '11', `h1` is set to the corresponding hour and `time` is 'AM'. If `h` is '12', `h1` is set to '12' and `time` is 'PM'. If `h` is '13' to '23', `h1` is set to the corresponding 12-hour format hour (from '01' to '11') and `time` is 'PM'. If `h` is '00', `h1` is set to '12' and `time` is 'AM'. The loop will print the formatted time for each input string.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the input, which represents the number of time conversions to be performed. For each of the `t` iterations, it reads a string `s` in the format "hh:mm" from the input, converts the hour part of `s` to a 12-hour format, and prints the converted time along with 'AM' or 'PM'. The final state of the program after the function concludes is that `t` iterations have been completed, and for each input string, the corresponding 12-hour formatted time has been printed.

