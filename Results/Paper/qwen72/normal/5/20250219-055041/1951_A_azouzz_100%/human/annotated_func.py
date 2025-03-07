#State of the program right berfore the function call: The function `generate_files_for_html_in_range` expects `start` and `end` to be integers where `start` is less than or equal to `end`. The current working directory should contain subfolders, and the names of these subfolders should be convertible to integers. The subfolders may contain files, and the function will specifically look for files with a `.html` extension.
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
        
    #State: `t` is 0, `n` is an input integer, `s` is a new input string for each iteration, `cnt1` is the number of occurrences of '1' in `s` for each iteration, and `_` is `t-1`. The state of the variables `start`, `end`, and the current working directory with subfolders and their contents remains unchanged.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the user input, which represents the number of test cases. For each test case, it reads another integer `n` and a string `s`. It then counts the number of '1's in `s` and prints 'YES' if the count is greater than 2 and even, or if the count is less than or equal to 2 and does not contain '11'. Otherwise, it prints 'NO'. The function does not modify any external state or return any values.

