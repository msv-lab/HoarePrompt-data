#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings consisting of exactly n lowercase Latin letters.
def func():
    tests = int(input())
    for i in range(tests):
        slength = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        no = True
        
        if c == a or c == b:
            no = False
            print('NO')
        else:
            for x in c:
                if x not in a and x not in b:
                    print('YES')
                    no = False
                    break
        
        if no:
            print('NO')
        
    #State: Output State: `tests` must be an integer between 1 and 1000 inclusive, `i` will be equal to the total number of iterations performed (which is the value of `tests`), `slength` remains the same as the initial input integer, `a` remains the same as the last input string, `b` remains the same as the last input string, `c` remains the same as the last input string, and `no` will be `False` if any character in `c` is found in either `a` or `b`. If no character in `c` is found in both `a` and `b`, then `no` will remain `True`.
    #
    #This means that after all iterations of the loop have finished, `tests` will hold the final value it had after the last iteration, `i` will reflect the total number of iterations (`tests`), and `no` will indicate whether there was any character in `c` that was not present in either `a` or `b` during any of the iterations. The values of `slength`, `a`, `b`, and `c` will be those provided in the last set of inputs processed by the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (number of test cases), an integer `n` (length of strings), and three strings `a`, `b`, and `c` (each of length `n`). For each test case, it checks if any character in `c` is present in either `a` or `b`. If any character in `c` is found in either `a` or `b`, it prints 'NO'. Otherwise, it checks if any character in `c` is not present in both `a` and `b`. If such a character exists, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function outputs the results for each test case.

