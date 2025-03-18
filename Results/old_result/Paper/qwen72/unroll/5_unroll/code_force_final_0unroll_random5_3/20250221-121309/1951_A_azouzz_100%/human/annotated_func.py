#State of the program right berfore the function call: start and end are integers, with start <= end. The current directory contains subfolders, and some of these subfolders are named with digits. Each subfolder may contain `.html` files.
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
        
    #State: The values of `start`, `end`, and `t` remain unchanged. The loop prints 'YES' or 'NO' based on the input values of `n` and `s` for each iteration, but does not modify any variables outside the loop.
#Overall this is what the function does:The function `func_1` reads an integer `t` from user input, which represents the number of test cases. For each test case, it reads another integer `n` and a string `s` from user input. It then checks the string `s` for the count of '1' characters and the presence of the substring '11'. Based on these conditions, it prints 'YES' or 'NO' for each test case. The function does not modify any variables outside the loop and does not interact with the file system or subfolders.

