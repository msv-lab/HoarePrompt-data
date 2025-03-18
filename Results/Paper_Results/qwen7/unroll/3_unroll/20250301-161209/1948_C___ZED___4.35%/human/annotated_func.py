#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; each test case consists of two strings of length n, where each character is either '<' or '>', representing the arrows in the first and second rows of the grid respectively.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; each test case consists of two strings of length n, where each character is either '<' or '>', representing the arrows in the first and second rows of the grid respectively; after processing all test cases, the output contains 'YES' or 'NO' for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and two strings of length `n`, where each character is either '<' or '>'. It then checks specific conditions related to the characters in these strings. If certain conditions are met, it prints 'YES', otherwise it prints 'NO'. After processing all test cases, the function outputs 'YES' or 'NO' for each case based on the specified conditions.

