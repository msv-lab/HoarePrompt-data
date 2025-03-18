#State of the program right berfore the function call: The function `func` is expected to take input through standard input and output through standard output, where the input consists of multiple test cases. Each test case starts with an integer n representing the number of piles, followed by a list of n integers representing the number of stones in each pile. The function should handle the input and output as described in the problem statement.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = map(int, input().split())
        
        lis = sorted(set(l))
        
        if 1 not in lis or len(lis) == 1:
            print('Alice')
        else:
            test = True
            for j in range(1, len(lis)):
                if lis[j] - lis[j - 1] > 1:
                    if j % 2 == 1:
                        print('Bob')
                    else:
                        print('Alice')
                    test = False
                    break
            if test == True:
                if len(lis) % 2 == 1:
                    print('Alice')
                else:
                    print('Bob')
        
    #State: The loop has finished executing all iterations, and the output for each test case has been printed to the standard output. The variable `t` is now 0, as all test cases have been processed. The variables `n`, `l`, `lis`, and `test` are no longer in scope and have been reset or are undefined.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case consists of an integer `n` and a list of `n` integers representing the number of stones in each pile. It processes these inputs and determines the winner of a game based on the rules provided. The function prints the winner ('Alice' or 'Bob') for each test case to standard output. After processing all test cases, the function exits, and the output for each test case has been printed. The internal variables used within the function are no longer in scope and are undefined.

