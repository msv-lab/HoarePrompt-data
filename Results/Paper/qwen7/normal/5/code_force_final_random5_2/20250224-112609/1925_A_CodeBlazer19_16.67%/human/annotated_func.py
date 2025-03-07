#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 676, and for each test case, n and k are positive integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
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
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 676\), `i` is 676, `n` is the first integer from the input split by space and converted to an integer, `k` is the second integer from the input split by space and converted to an integer, `s` is the string containing all lowercase letters from the 97th to the \(k+96\)th ASCII character, and `j` is the next ASCII character after `k` + 96.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: t, n, and k. For each test case, it constructs a string `s` containing lowercase letters from 'a' to the letter corresponding to `k`. If `k` equals 1, it prints `n` times the string `s`. Otherwise, it prints `(2 - (n == 1))` times the string `s`. The function does not return any value but prints the result for each test case.

