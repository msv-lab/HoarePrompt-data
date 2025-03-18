#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and s is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format, where hh is an integer from 00 to 23 and mm is an integer from 00 to 59.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1440, `s` is a user-provided string of length 5 in the format "hh:mm" representing a valid time in 24-hour format, and `h` is the substring of `s` from index 0 to 1 (inclusive). The loop has executed `t` times, and for each iteration, the hour part of the time has been converted to 12-hour format and printed with AM/PM notation. The final state of `t` is 0, and the final state of `s` and `h` is the last user-provided values before the loop ended.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, followed by `t` strings `s` each representing a time in 24-hour format ("hh:mm"). For each input time, it converts the hour part to 12-hour format and appends "AM" or "PM" based on the original hour value, then prints the converted time. The function does not return any value; it only prints the results. After the function concludes, `t` test cases have been processed, and the final state of `t` is 0, while `s` and `h` hold the last user-provided values before the loop ended.

