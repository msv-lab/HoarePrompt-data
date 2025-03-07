#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and s is a string of length 5 in the format "hh:mm" where hh is an integer from 00 to 23 and mm is an integer from 00 to 59, representing a valid time in 24-hour format.
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
        
    #State: After the loop has executed all iterations, `t` is an integer such that the number of iterations performed equals the initial value of `t`. For each iteration, `s` was a string of length 5 in the format "hh:mm", where `hh` is an integer from 00 to 23 and `mm` is an integer from 00 to 59, representing a valid time in 24-hour format. The loop converted each `s` to a 12-hour format with AM/PM notation and printed it. The final state of `t` is 0, as the loop has completed all its iterations, and `s` and `h` are no longer relevant as they are redefined in each iteration.
#Overall this is what the function does:The function reads an integer `t` (1 ≤ t ≤ 1440) indicating the number of times it will process a time string. For each of these `t` times, it reads a string `s` in the format "hh:mm" representing a valid time in 24-hour format. It converts each `s` to a 12-hour format with AM/PM notation and prints the converted time. The function does not return any value; it only prints the converted times. After all iterations, the function completes, and the final state is that `t` iterations have been performed, and the converted times have been printed.

