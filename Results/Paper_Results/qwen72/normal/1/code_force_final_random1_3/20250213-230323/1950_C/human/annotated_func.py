#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1440, and s is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format, where hh is the hour (00 to 23) and mm is the minute (00 to 59).
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
        
    #State: `t` is an integer where `t` equals the initial value of `t` provided as input, and `s` is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format. The loop has completed all its iterations, and the program has printed the converted time for each input `s` in 12-hour format followed by 'AM' or 'PM'. The variable `h` is no longer relevant as it is recalculated in each iteration based on the new input `s`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of times it will process a time string `s` in the format "hh:mm". For each `s`, it converts the time from 24-hour format to 12-hour format and appends 'AM' or 'PM' accordingly, printing the result directly. After processing all inputs, the function completes without returning any value, leaving the input variables `t` and `s` unchanged.

