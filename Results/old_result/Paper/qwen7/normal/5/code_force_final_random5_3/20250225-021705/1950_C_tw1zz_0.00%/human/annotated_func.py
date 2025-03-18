#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in the 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
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
        
    #State: Output State: The loop will continue to run until all possible inputs for the time format "hh:mm" have been processed. Since the code provided processes one time input per iteration, and there are no constraints on the number of iterations beyond the input itself, the loop will terminate when all valid times have been inputted.
    #
    #In the final output state after all iterations of the loop have finished, the following conditions will hold true:
    #- `s` is a string of length 5 in the format "hh:mm".
    #- `t` is an integer such that 1 ≤ t ≤ 1440.
    #- `h1` will be the 12-hour format representation of the hour part of the last time input, which could be any value from '01' to '12'.
    #- `m1` will be the minute part of the last time input as a string.
    #- `time` will be either 'AM' or 'PM', depending on whether the hour part of the last time input is less than '12' or not.
    #
    #The loop processes each valid time input independently, so the final state depends solely on the last input provided.
#Overall this is what the function does:The function processes multiple time inputs in the format "hh:mm" and converts them to 12-hour format with AM/PM notation. After processing all inputs, it prints each time in the format "h1:mm  time", where `h1` is the converted hour, `mm` is the minute, and `time` is either 'AM' or 'PM'. The function does not return any value; its primary action is to print the converted times.

