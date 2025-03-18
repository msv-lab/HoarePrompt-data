#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: Output State: The output state will consist of a series of numbers printed based on the condition `n if n - k <= 1 else 1` for each test case. For each test case, if the difference between `n` and `k` is less than or equal to 1, the number `n` will be printed; otherwise, the number `1` will be printed. The total number of outputs will be equal to the number of test cases provided by the input.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it prints \( n \) if the difference between \( n \) and \( k \) is less than or equal to 1; otherwise, it prints 1. The function reads the number of test cases from the first line of input and then reads the values of \( n \) and \( k \) for each test case. The final state of the program is a series of printed outputs based on the given condition.

