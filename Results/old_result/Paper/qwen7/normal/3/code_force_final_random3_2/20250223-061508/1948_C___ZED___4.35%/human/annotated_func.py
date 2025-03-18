#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; the first line of each test case contains a string of length n consisting of characters '<' and/or '>'; the second line of each test case contains a string of length n consisting of characters '<' and/or '>'.
def func():
    for i in range(int(input())):
        n = int(input())
        
        a = input()
        
        b = input()
        
        if b[-2] != '>':
            print('NO')
        elif n == 1:
            print('YES')
        else:
            no_path = True
            for k in range(0, n, 2):
                if b[k] != '>':
                    no_path = False
            if not no_path:
                no_path = True
                for k in range(1, n - 1, 2):
                    print(k)
                    if a[k] != '>':
                        no_path = False
            if no_path:
                print('YES')
            else:
                print('NO')
        
    #State: After the loop executes all iterations, `i` is equal to the total number of test cases, `n` is an integer greater than or equal to 4 for each test case, `b` remains the same as the input string for each test case, and `no_path` remains `False` unless the last second character of `b` is `'>';` in that case, `no_path` becomes `True`.
#Overall this is what the function does:The function processes multiple test cases, each containing two strings of equal even length consisting only of '<' and '>'. For each test case, it checks if the second-to-last character of the second string is '>', and if the length of the string is 2 or more. If these conditions are met, it further checks if the characters at specific positions in the strings meet certain criteria. Based on these checks, it prints either 'YES' or 'NO' for each test case.

