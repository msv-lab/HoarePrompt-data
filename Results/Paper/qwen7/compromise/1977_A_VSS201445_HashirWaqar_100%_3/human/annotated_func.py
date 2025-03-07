#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' based on the condition `if n >= m and (n - m) % 2 == 0`. For each test case provided by the input, if `n` is greater than or equal to `m` and the difference between `n` and `m` is even, it prints 'YES', otherwise it prints 'NO'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( n \) and \( m \). For each test case, it checks if \( n \) is greater than or equal to \( m \) and if the difference between \( n \) and \( m \) is even. If both conditions are met, it outputs 'YES'; otherwise, it outputs 'NO'. The function reads the number of test cases from the first line of input and the values of \( n \) and \( m \) for each test case from subsequent lines.

