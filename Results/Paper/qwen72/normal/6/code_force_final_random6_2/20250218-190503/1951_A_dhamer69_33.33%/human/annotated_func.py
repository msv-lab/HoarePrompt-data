#State of the program right berfore the function call: start and end are integers, where start <= end, and the current directory contains subfolders that can be represented as integers within the range [start, end].
def func():
    t = int(input())
    while t > 0:
        n = int(input())
        
        s = input()
        
        if n == 2:
            if s == '00':
                print('YES')
            else:
                print('NO')
        else:
            count_1 = s.count('1')
            if count_1 % 2 != 0:
                print('NO')
            elif s.count('11') == 1:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: `start` and `end` are integers where `start` <= `end`, the current directory contains subfolders that can be represented as integers within the range [start, end], `t` is 0, and the loop has executed `t` times, where `t` is the initial value of `t`. For each iteration, `n` was an input integer, and `s` was an input string. If `n` was 2, the program checked if `s` was '00' and printed 'YES' if true, otherwise 'NO'. If `n` was not 2, the program counted the number of '1' characters in `s` and checked if this count was odd or if the count was even and `s` contained exactly one occurrence of '11'. If either condition was true, the program printed 'NO'. Otherwise, it printed 'YES'.
#Overall this is what the function does:The function reads an integer `t` from the user, and for each of the `t` iterations, it reads another integer `n` and a string `s`. If `n` is 2, it prints 'YES' if `s` is '00', otherwise it prints 'NO'. If `n` is not 2, it prints 'NO' if the number of '1' characters in `s` is odd or if `s` contains exactly one occurrence of '11'. Otherwise, it prints 'YES'. After `t` iterations, the function terminates, and `t` is 0. The function does not return any value.

