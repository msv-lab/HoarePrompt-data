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
        
    #State: Output State: The loop will continue to execute for as many times as specified by the user via the input. After all iterations, `h` will be an empty string (`''`), `m` will be an empty string (`''`), `h1` will be one of the strings '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', or '00', `m1` will be an empty string (`''`), and `time` will be either 'AM' or 'PM'. 
    #
    #This is because each iteration of the loop processes a new input time, updates the variables `h1` and `time` based on the rules provided, and then prints these updated values before moving on to the next iteration. By the end of all iterations, all the input times have been processed, and the final state of the variables will reflect the last input time's transformation into 12-hour format with AM/PM designation.
#Overall this is what the function does:The function processes multiple time inputs in the 24-hour format and converts them into the 12-hour format with AM/PM designations. It reads the number of test cases from the first input, then for each test case, it takes a time string in the format "hh:mm", converts the hour part into the 12-hour format, and prints the result along with the appropriate AM/PM designation. After processing all the test cases, the function does not return any value but outputs the converted times.

