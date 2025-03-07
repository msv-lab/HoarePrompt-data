#State of the program right berfore the function call: The function should take an integer t (1 ≤ t ≤ 50) representing the number of test cases, and for each test case, an integer n (1 ≤ n ≤ 50) representing the number of special characters required in the string.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = 'AAB' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: The variable `t` remains an integer between 1 and 50, inclusive, representing the number of test cases. The loop has completed all its iterations, and the values of `n` and `s` are no longer relevant as they are redefined in each iteration.
#Overall this is what the function does:The function `func` accepts an integer `t` (1 ≤ t ≤ 50) representing the number of test cases. For each test case, it accepts another integer `n` (1 ≤ n ≤ 50) representing the number of special characters required in the string. The function prints 'NO' if `n` is odd or if the length of the generated string exceeds 200 characters. If `n` is even and the length of the string is within the limit, it prints 'YES' followed by the string, which consists of the pattern 'AAB' repeated `n // 2` times. After all test cases are processed, the function concludes without returning any value.

