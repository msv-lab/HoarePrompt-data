#State of the program right berfore the function call: The function should take a string s as input, where s is a valid time in 24-hour format (hh:mm) with hh ranging from 00 to 23 and mm ranging from 00 to 59. The function should also handle multiple test cases, indicated by an integer t (1 ≤ t ≤ 1440).
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
        
    #State: Output State: The function will take the input string `s` representing a time in 24-hour format (hh:mm) and convert it to a 12-hour format with AM/PM notation. For each test case, it will print the converted time. The variables `h1`, `m1`, and `time` will be updated for each iteration based on the input time, and the final state of these variables will depend on the last input time processed. The loop will execute `t` times, where `t` is the number of test cases provided. After the loop finishes, the state of `h1`, `m1`, and `time` will reflect the last time conversion performed. The initial state of `s` and `t` will remain unchanged. 
    #
    #For example, if the input is:
    #```
    #3
    #01:15
    #13:30
    #23:45
    #```
    #The output will be:
    #```
    #01:15 AM
    #01:30 PM
    #11:45 PM
    #```
    #And the final state of the variables will be:
    #- `h1` = '11'
    #- `m1` = '45'
    #- `time` = 'PM'
#Overall this is what the function does:The function `func` reads an integer `t` from the input, indicating the number of test cases (1 ≤ t ≤ 1440). For each test case, it reads a string `s` in 24-hour format (hh:mm) and converts it to a 12-hour format with AM/PM notation. It then prints the converted time for each test case. The function does not return any value. After the function concludes, the variables `h1`, `m1`, and `time` will reflect the last time conversion performed, and the initial state of the input values will remain unchanged.

