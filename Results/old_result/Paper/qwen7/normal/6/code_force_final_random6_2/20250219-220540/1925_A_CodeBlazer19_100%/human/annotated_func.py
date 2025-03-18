#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 676, and for each test case, n and k are positive integers satisfying 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: Output State: The loop will have executed all iterations, meaning `i` will be equal to `t-1`. For each iteration, `n` and `k` are integers input by the user, and the output will consist of the string `'abcdefghijklmnopqrstuvwxyz'[:k]` repeated `n` times. The value of `t` will be the same as it was initially, and it must still satisfy the condition 1 ≤ `t` ≤ 676.
#Overall this is what the function does:The function processes a series of test cases defined by the variable `t`. For each test case, it reads two integers `n` and `k` from the input. It then prints a string consisting of the first `k` characters of the alphabet ('a' to 'z') repeated `n` times. After processing all test cases, the function concludes with the original value of `t` remaining unchanged within the specified range (1 ≤ `t` ≤ 676).

