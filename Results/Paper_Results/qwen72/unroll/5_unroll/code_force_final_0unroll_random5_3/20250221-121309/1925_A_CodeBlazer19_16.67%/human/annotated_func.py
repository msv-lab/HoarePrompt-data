#State of the program right berfore the function call: The function `func` does not take any input parameters, but it is expected to handle multiple test cases. Each test case consists of two integers, n and k, where 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26. The function should internally read the number of test cases t (1 ≤ t ≤ 676) and the values of n and k for each test case.
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
        
    #State: The loop has executed `t` times, and for each iteration, it has read two integers `n` and `k` from the input. If `k` is 1, it prints `n` times the string consisting of the character 'a'. If `k` is greater than 1, it prints the string consisting of the first `k` characters of the English alphabet, repeated twice unless `n` is 1, in which case it is repeated once. The variables `n`, `k`, and `t` are unchanged after the loop, but the input has been consumed and the corresponding output has been printed for each test case.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads a number of test cases `t` (1 ≤ t ≤ 676) from the input. For each test case, it reads two integers `n` and `k` (1 ≤ n, k ≤ 26). If `k` is 1, it prints a string consisting of `n` times the character 'a'. If `k` is greater than 1, it prints a string consisting of the first `k` characters of the English alphabet, repeated twice unless `n` is 1, in which case it is repeated once. The function does not return any value; it only prints the results to the output.

