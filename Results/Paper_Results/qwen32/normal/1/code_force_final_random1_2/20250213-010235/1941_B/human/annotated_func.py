#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 3 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_j ≤ 10^9. The sum of all n across all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: The program will have printed "YES" or "NO" for each of the `t` test cases based on the conditions specified in the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it checks specific conditions related to the parity and consecutive differences of the first and last elements of the list `a`. It prints "YES" if the conditions are met, otherwise it prints "NO".

