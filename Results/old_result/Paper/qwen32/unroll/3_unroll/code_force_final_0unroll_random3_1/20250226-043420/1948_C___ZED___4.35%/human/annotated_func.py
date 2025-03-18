#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an even integer such that 2 <= n <= 2 * 10^5, and the sum of n over all test cases does not exceed 2 * 10^5. The first and second lines of each test case contain strings of length n consisting of characters '<' and/or '>', representing the arrows in the first and second rows of the grid, respectively.
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
        
    #State: - The output state consists of 'YES' or 'NO' for each test case based on the conditions mentioned above.
    #   - The variables `t`, `n`, `a`, and `b` are modified during each iteration of the loop, but the final output state is determined by the printed results for each test case.
    #
    #Given the initial state and the behavior of the loop, the output state will be a series of 'YES' or 'NO' printed for each test case.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each consisting of two strings of equal even length containing '<' and/or '>' characters. For each test case, it determines whether it's possible to match each '>' in the second string with a '<' in the first string such that each pair of matched characters are facing each other. The function outputs 'YES' if such a matching is possible for a test case and 'NO' otherwise.

