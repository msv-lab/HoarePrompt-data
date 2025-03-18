#State of the program right berfore the function call: The function should accept an integer t (1 ≤ t ≤ 50) representing the number of test cases, and for each test case, an integer n (1 ≤ n ≤ 50) representing the number of special characters required in the string.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            print('YES')
            pattern = []
            for i in range(n // 2):
                pattern.append('AB'[i % 2])
                pattern.append('AB'[i % 2 ^ 1])
            print(''.join(pattern))
        
    #State: The loop has finished executing for all `t` test cases. For each test case, if `n` is odd, 'NO' is printed. If `n` is even, 'YES' is printed followed by a string of length `n` that alternates between 'A' and 'B'. The variable `t` remains unchanged, and the variable `n` is not retained after each iteration.
#Overall this is what the function does:The function `func` accepts no parameters. It reads an integer `t` (1 ≤ t ≤ 50) from the input, representing the number of test cases. For each test case, it reads another integer `n` (1 ≤ n ≤ 50) from the input, representing the number of special characters required in the string. For each test case, if `n` is odd, it prints 'NO'. If `n` is even, it prints 'YES' followed by a string of length `n` that alternates between 'A' and 'B'. After processing all test cases, the function completes and does not return any value. The state of the program after the function concludes is that `t` test cases have been processed, and the appropriate output has been printed for each case.

