#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end.
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
        
    #State: `start` and `end` are integers such that 0 <= `start` <= `end`, `t` is 0, `n` is an input integer, `s` is an input string. If `n` is 2, the state of `s` and the other variables remains unchanged. If `n` is not 2, `count_1` is the number of occurrences of the character '1' in `s`. If `count_1` is odd, the current value of `count_1` remains odd. If `count_1` is even, the current value of `count_1` remains even. Additionally, if `s` contains exactly one occurrence of the substring '11', this condition is retained. Otherwise, the number of occurrences of the substring '11' in `s` is not equal to 1.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the user, representing the number of test cases. For each test case, it reads an integer `n` and a string `s` from the user. The function then checks if the string `s` meets certain conditions based on the value of `n`. If `n` is 2, it prints 'YES' if `s` is '00', otherwise it prints 'NO'. If `n` is not 2, it prints 'NO' if the number of '1's in `s` is odd or if the substring '11' appears exactly once in `s`. Otherwise, it prints 'YES'. After processing all test cases, the function concludes with `t` being 0.

