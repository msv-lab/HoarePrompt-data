#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of an integer n such that 2 <= n <= 2 * 10^5 and n is even. The following two lines for each test case contain strings of length n consisting of characters '<' and '>', representing the arrows in the first and second rows of the grid, respectively. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `i` is equal to `t-1` (indicating all iterations have completed), `n` is the integer from the last test case, `a` is the string from the last test case, and `b` is the string from the last test case. The loop has processed all `t` test cases, and for each test case, it has printed either 'YES' or 'NO' based on the conditions specified in the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an even integer `n` and two strings of length `n` made up of '<' and '>' characters. It prints 'YES' if it is possible to make the grid valid by potentially reversing some arrows, such that no two arrows point towards each other in the same column, and 'NO' otherwise.

