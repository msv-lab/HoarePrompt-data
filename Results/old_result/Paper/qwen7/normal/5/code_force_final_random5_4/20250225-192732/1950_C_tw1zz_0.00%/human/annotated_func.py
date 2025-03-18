#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
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
        
    #State: Output State: All inputs to the loop have been processed, and for each input, the output is a string in the format "h1:mm AM/PM". Here, `h1` is the adjusted hour part of the input time, `mm` is the original minute part of the time, and `AM/PM` is determined based on the value of `h1`. Specifically:
    #
    #- If `h1` is '01', '02', '03', '04', '05', '06', '07', '08', or '09', the time is in the AM period.
    #- If `h1` is '10', '11', or '12', the time is in the PM period.
    #
    #The variable `t` has been decremented to zero after all iterations of the loop have completed. The variables `h`, `m`, `h1`, `m1`, and `time` reflect the final processed input from the loop.
#Overall this is what the function does:The function processes multiple time inputs in 24-hour format and converts them to 12-hour format with AM/PM notation. For each input, it prints the time in the format "h1:mm AM/PM", where `h1` is the adjusted hour, `mm` is the minute, and `AM/PM` is determined based on the adjusted hour. After processing all inputs, the function ensures that all time conversions are correctly displayed according to the 12-hour clock system.

