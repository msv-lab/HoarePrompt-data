#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' strings printed based on the condition `(n - m) % 2 == 0` and `n >= m` for each test case provided by the user. Each test case is defined by two integers `n` and `m`, and the loop will execute `int(input())` times, where `input()` reads the number of test cases from the user.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: t (number of test cases), n, and m. For each test case, it checks if n is greater than or equal to m and if (n - m) is divisible by 2. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function concludes with the output containing a series of 'YES' and 'NO' strings corresponding to each test case.

