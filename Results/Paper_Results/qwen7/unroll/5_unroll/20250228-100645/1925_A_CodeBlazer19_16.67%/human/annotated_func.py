#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 676, and for each test case, n and k are positive integers satisfying 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        s = ''
        
        for j in range(97, k + 97):
            s += chr(j)
        
        if k == 1:
            print(n * s)
        else:
            print((2 - (n == 1)) * s)
        
    #State: Output State: The output state will consist of multiple strings printed based on the input values provided within the specified constraints. For each iteration of the outer loop (controlled by `t`), the program reads two integers `n` and `k` from the input. It then generates a string `s` containing `k` lowercase letters starting from 'a'. If `k` is 1, it prints `n` times the character 'a'. Otherwise, it prints `(2 - (n == 1))` times the string `s`. The total number of strings printed will be equal to the value of `t`. Each string printed depends on the specific values of `n` and `k` for that iteration.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers \( n \) and \( k \) where \( 1 \leq n \leq 26 \) and \( 1 \leq k \leq 26 \). For each test case, it generates a string consisting of \( k \) lowercase letters starting from 'a'. If \( k \) is 1, it prints the character 'a' repeated \( n \) times; otherwise, it prints the generated string repeated \( (2 - (n == 1)) \) times. The function outputs multiple strings, one for each test case, based on the given inputs.

