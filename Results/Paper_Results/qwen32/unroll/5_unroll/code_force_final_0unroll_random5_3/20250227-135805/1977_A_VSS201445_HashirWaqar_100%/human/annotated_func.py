#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each of the t test cases, n and m are integers such that 1 ≤ n, m ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: For each of the t test cases, the program will output either 'YES' or 'NO' based on whether n is greater than or equal to m and (n - m) is even. The values of t, n, and m will remain as per the input, but the program will have printed the result for each test case.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it checks if the integer `n` is greater than or equal to the integer `m` and if the difference `(n - m)` is even. It prints 'YES' if both conditions are met, otherwise it prints 'NO'. The values of `t`, `n`, and `m` remain unchanged after processing each test case.

