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
        
    #State: `start` and `end` are integers where `start <= end`, `t` is 0, `_` is a placeholder (no specific state), `n` is an input integer, `s` is an input string, and `cnt1` is the number of occurrences of '1' in `s`. For each iteration, if `cnt1` is greater than 2 and even, the condition is met and 'YES' is printed. If `cnt1` is greater than 2 and odd, or if `cnt1` is 1, the condition is also met and 'NO' is printed. If '11' is in `s`, the string `s` contains the substring '11' and 'NO' is printed. Otherwise, 'YES' is printed.
#Overall this is what the function does:The function `func_1` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a string `s` of length `n`. It then evaluates the string `s` based on the count of '1' characters and the presence of the substring '11'. If the count of '1' is greater than 2 and even, or if the count is 2 or less, it prints 'YES'. If the count of '1' is greater than 2 and odd, or if the substring '11' is present in `s`, it prints 'NO'. The function does not modify any external state or variables outside its scope.

