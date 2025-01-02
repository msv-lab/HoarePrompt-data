#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n integers where each a_i is either 0 or 1. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func():
    t = int(raw_input())
    for _ in range(t):
        n = int(raw_input())
        
        A = map(int, raw_input().split())
        
        A.reverse()
        
        F = [0] * n
        
        M = [0] * n
        
        F[0] = A[0]
        
        if n == 1:
            print(F[0])
            continue
        
        F[1] = A[1]
        
        for i in range(2, n):
            M[i] = min(F[i - 1], F[i - 2])
            F[i] = min(A[i] + M[i - 1], A[i] + A[i - 1] + M[i - 2])
        
        print(F[-1])
        
    #State of the program after the  for loop has been executed: `t` is an integer such that 1 ≤ t ≤ 2 ⋅ 10^4, `_` is `t - 1`, `n` is an input integer, `A` is a map object containing integers from the last input line in reversed order, `F` is a list of length `n` where `F[0] = A[0]`, `F[1] = A[1]`, and for `i` in range(2, n), `F[i] = min(A[i] + M[i - 1], A[i] + A[i - 1] + M[i - 2])`, `M` is a list of length `n` where for `i` in range(2, n), `M[i] = min(F[i - 1], F[i - 2])`. If `n == 1`, `F` is `[A[0]]` and `M` is `[0]`. For each iteration of the loop, the value of `F[-1]` has been printed.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, processes each test case, and prints the result for each one. Each test case consists of an integer `n` followed by a list of `n` integers (each being 0 or 1). The function calculates the minimum cost to traverse the list from the start to the end, where the cost of moving to the next element is determined by the values in the list. The function prints the minimum cost for each test case. After processing all test cases, the function terminates. The state of the program after the function concludes is that `t` is an integer such that 1 ≤ t ≤ 2 ⋅ 10^4, `_` is `t - 1`, `n` is the last input integer, `A` is a list of the last input integers in reversed order, `F` and `M` are lists of length `n` used for dynamic programming calculations, and the results for each test case have been printed. Edge cases include when `n` is 1, in which case the function directly prints the first element of `A`.

