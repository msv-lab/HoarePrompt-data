#State of the program right berfore the function call: start and end are integers where start <= end, and they represent the range of folder names to be processed. The current directory contains subfolders, some of which may contain .html files.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2 and (cnt1 % 2 == 1 or cnt1 == 1):
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: `start` and `end` are integers where `start` <= `end`, representing the range of folder names to be processed, the current directory contains subfolders, some of which may contain .html files, `t` is the original input value, `_` is `t-1`, `n` is the last input integer, `s` is the last input string, and `cnt1` is the number of occurrences of '1' in the last input string `s`. If `cnt1` is greater than 2 and even, the program prints 'YES'. If `cnt1` is greater than 2 and either odd or 1, the program prints 'NO'. If `cnt1` is not greater than 2 or `cnt1` is even and not 1, and if '11' is in `s`, the program prints 'NO'. If '11' is not in `s`, the program prints 'YES'.
#Overall this is what the function does:The function `func_1` processes a series of inputs. It reads an integer `t` indicating the number of test cases. For each test case, it reads another integer `n` and a string `s`. Based on the count of '1' characters in `s` and the presence of the substring '11', it prints 'YES' or 'NO' for each test case. The function does not modify any external state or return any values.

