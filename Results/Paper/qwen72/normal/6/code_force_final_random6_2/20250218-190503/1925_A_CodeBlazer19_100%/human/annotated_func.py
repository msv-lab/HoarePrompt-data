#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases, where each test case consists of two positive integers n and k such that 1 <= n <= 26 and 1 <= k <= 26. The function should be designed to read input from stdin and write output to stdout, handling the specified range of inputs.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: `t` is 0, `i` is `t-1`, `n` and `k` are input integers.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input (`stdin`), where each test case consists of two positive integers `n` and `k` (1 <= n, k <= 26). For each test case, it generates a string by repeating the first `k` letters of the English alphabet `n` times and prints this string to standard output (`stdout`). After processing all test cases, the function completes execution, and the variables `t`, `i`, `n`, and `k` are no longer in use.

