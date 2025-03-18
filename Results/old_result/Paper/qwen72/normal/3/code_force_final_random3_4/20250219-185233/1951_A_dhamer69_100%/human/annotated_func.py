#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end, and they represent the range of folder names to be checked for generating files.
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
            elif s.count('11') == 1 and count_1 == 2:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: `start` and `end` are integers such that 0 <= `start` <= `end`, `t` is 0, `n` is an input integer, and `s` is a new input string. If `n` == 2, the program checks if `s` is '00' and prints 'YES' if true, otherwise 'NO'. If `n` != 2, the program counts the number of '1' characters in `s` (`count_1`). If `count_1` is odd or if `s` contains exactly one occurrence of '11' and exactly two '1' characters, the program prints 'NO'. Otherwise, the program prints 'YES'. The state of `start` and `end` remains unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads an integer `n` and a string `s` from the user. The function then checks the string `s` based on the value of `n` and prints 'YES' or 'NO' accordingly. Specifically, if `n` is 2, it prints 'YES' if `s` is '00', otherwise 'NO'. If `n` is not 2, it prints 'NO' if the number of '1' characters in `s` is odd or if `s` contains exactly one occurrence of '11' and exactly two '1' characters; otherwise, it prints 'YES'. After processing all test cases, the function concludes with no further actions or side effects.

