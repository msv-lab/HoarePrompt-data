#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; each test case consists of two strings of length n, where each character in the strings is either '<' or '>', representing the arrows in the first and second rows of the grid, respectively.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; each test case consists of two strings of length n, where each character in the strings is either '<' or '>', representing the arrows in the first and second rows of the grid, respectively; after executing all iterations of the loop, the output consists of 'YES' or 'NO' based on the conditions specified in the loop body.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two strings of length n (where n is even), containing characters '<' or '>'. For each test case, it checks if a path exists from the top row to the bottom row following the direction of the arrows. If a valid path is found, it prints 'YES'; otherwise, it prints 'NO'. The function reads input values for the number of test cases and for each test case, it reads the two strings. After processing all test cases, it outputs the result for each case.

