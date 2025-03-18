#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 676, and for each test case, n and k are positive integers satisfying 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: Output State: The output consists of multiple lines, each containing a string of length `n*k` made up of the first `k` letters of the alphabet ('a' to 'z'). The number of such lines is equal to the value of `t`. Each line is generated based on the input provided during each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each defined by positive integers `t`, `n`, and `k` (where 1 ≤ t ≤ 676, 1 ≤ n ≤ 26, and 1 ≤ k ≤ 26). For each test case, it generates and prints a string consisting of `n*k` characters, which are the first `k` letters of the English alphabet ('a' to 'z'), repeated as necessary to form the desired length. After processing all test cases, the function concludes with no explicit return value.

