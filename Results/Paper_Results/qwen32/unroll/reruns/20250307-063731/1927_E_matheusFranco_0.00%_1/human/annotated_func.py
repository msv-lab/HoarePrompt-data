#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n, and k is even.
def func_1():
    n, k = map(int, input().split(' '))
    permutation = [0] * n
    idx = 0
    idx_v = 1
    curr_v = 1
    for i in range(k):
        multiples_of_k_plus_i = i
        
        while multiples_of_k_plus_i < len(permutation):
            permutation[multiples_of_k_plus_i] = curr_v
            curr_v += 1
            multiples_of_k_plus_i += k
        
    #State: permutation is a list of length `n` filled with values from 1 to the total number of elements filled according to the loop's behavior, `curr_v` is the next value to be assigned after the loop completes, `idx` is 0, `idx_v` is 1.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: result (where result is the space-separated concatenation of the elements of the `permutation` list, which contains numbers from 1 to n)
#Overall this is what the function does:The function reads two integers `n` and `k` from the input, where `2 <= k <= n` and `k` is even. It constructs a permutation list of length `n` by filling it with values in a specific pattern based on multiples of `k`, starting from 1. Finally, it prints the permutation as a space-separated string.

#State of the program right berfore the function call: This function does not have any parameters in its signature. It reads input from the standard input, which consists of multiple test cases. Each test case contains two integers, n and k, where 2 <= k <= n <= 2 * 10^5 and k is even. The variable t represents the number of test cases (1 <= t <= 10^4).
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of two integers, `n` and `k`. It processes each test case by calling `func_1()` and outputs the result for each case. After processing all test cases, it terminates.

