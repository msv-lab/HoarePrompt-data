#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an even integer such that 2 <= n <= 2 * 10^5, and there are two strings of length n consisting of '<' and '>' characters representing the arrows in the first and second rows of the grid, respectively. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: a series of 'YES' or 'NO' responses for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an even integer `n` and two strings of length `n` made up of '<' and '>' characters. For each test case, it determines whether there is a valid path based on the arrangement of the characters in the strings and outputs 'YES' or 'NO' accordingly.

