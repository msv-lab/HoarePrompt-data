#State of the program right berfore the function call: start and end are integers where start <= end, and they represent the range of folder names to be processed. The current directory contains subfolders named with digits, and some of these subfolders may contain .html files.
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
        
    #State: start and end are integers where start <= end, representing the range of folder names to be processed, the current directory contains subfolders named with digits, some of which may contain .html files, t is 0, n is the last input integer, s is the last input string, and `cnt1` is the number of occurrences of '1' in the last `s`. If `cnt1` is greater than 2 and is an even number, the condition is met. If `cnt1` is greater than 2 and is odd, or `cnt1` is 1, the condition is met. If `cnt1` is less than or equal to 2 or is even, and '11' is in the last `s`, the string '11' is present in the last `s`; otherwise, '11' is not a substring of the last `s`.
#Overall this is what the function does:The function `func_1` reads multiple sets of inputs from the user. For each set, it reads an integer `n` and a string `s`. It then counts the occurrences of the character '1' in the string `s`. Based on the count and the presence of the substring '11', it prints 'YES' or 'NO'. Specifically, it prints 'YES' if the count of '1' is greater than 2 and even, or if the count is 2 or less and '11' is not in the string. It prints 'NO' in all other cases. After processing all sets of inputs, the function ends without returning any value. The state of the program after the function concludes includes the last values of `t`, `n`, `s`, and `cnt1` as described in the annotations.

