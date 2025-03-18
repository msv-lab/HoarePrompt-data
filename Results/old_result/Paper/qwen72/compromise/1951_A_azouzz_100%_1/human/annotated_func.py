#State of the program right berfore the function call: start and end are integers such that start <= end, and they represent the range of folder names to be processed. The current directory contains subfolders, and the function processes only those subfolders whose names are digits and fall within the specified range [start, end].
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
        
    #State: The values of `start`, `end`, and `t` remain unchanged. The loop prints 'YES' or 'NO' for each iteration based on the input `n` and `s`, but does not modify any variables outside the loop.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads multiple test cases from the standard input, where each test case consists of an integer `n` and a string `s` of length `n`. For each test case, the function checks the count of '1' characters in `s` and prints 'YES' or 'NO' based on specific conditions: it prints 'YES' if the count of '1' is greater than 2 and even, or if the count is 0 or 1 and '11' is not a substring of `s`. Otherwise, it prints 'NO'. The function does not modify any external variables or state.

