#State of the program right berfore the function call: The function `generate_files_for_html_in_range` takes two integer arguments, `start` and `end`, such that `start` is less than or equal to `end`. These integers represent the range of folder names (which should be digits) to be considered for processing HTML files within the current working directory.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2:
            print('NO')
        elif cnt1 == 1:
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: `start` is an integer, `end` is an integer such that `start` is less than or equal to `end`, `t` is 0, `n` is the integer input by the user in the last iteration, `s` is the string input by the user in the last iteration, and `cnt1` is the number of occurrences of '1' in the last `s`. The loop has finished executing all `t` iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s`. It then counts the occurrences of '1' in the string `s`. Based on the count and the presence of '11' in the string, it prints 'YES' or 'NO'. The function does not process any files or directories.

