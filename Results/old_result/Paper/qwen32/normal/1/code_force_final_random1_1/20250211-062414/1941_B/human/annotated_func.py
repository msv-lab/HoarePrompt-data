#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 3 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each element a_j satisfies 0 ≤ a_j ≤ 10^9. The sum of all n across all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: A sequence of 'YES' or 'NO' printed for each test case based on the given conditions.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it checks specific conditions related to the parity and values of the first two and last two elements of the list `a`. It prints 'YES' if the conditions are met, otherwise it prints 'NO'.

