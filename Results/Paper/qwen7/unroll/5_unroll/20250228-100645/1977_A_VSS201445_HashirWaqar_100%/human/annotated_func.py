#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: The output consists of 'YES' or 'NO' printed for each test case based on the condition `if n >= m and (n - m) % 2 == 0`. Each line of output corresponds to the result of one test case provided by the input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers: t, n, and m. For each test case, it checks if n is greater than or equal to m and if (n - m) is divisible by 2. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints 'YES' or 'NO' for each test case based on the specified condition.

