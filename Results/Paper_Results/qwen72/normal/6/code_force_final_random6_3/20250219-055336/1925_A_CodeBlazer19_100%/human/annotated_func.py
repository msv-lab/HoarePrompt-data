#State of the program right berfore the function call: The function `func` is expected to read input from stdin, where the first line contains an integer t (1 ≤ t ≤ 676) representing the number of test cases. Each of the following t lines contains two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: `t` is an integer between 1 and 676, inclusive, `i` is `t-1`, `n` is the last input integer, `k` is the last input integer.
#Overall this is what the function does:The function `func` reads an integer `t` from standard input, representing the number of test cases. For each of the `t` test cases, it reads two integers `n` and `k` from standard input. It then prints a string that consists of the first `k` letters of the English alphabet repeated `n` times. After processing all test cases, the function concludes, and the final state of the program includes the printed results for each test case.

