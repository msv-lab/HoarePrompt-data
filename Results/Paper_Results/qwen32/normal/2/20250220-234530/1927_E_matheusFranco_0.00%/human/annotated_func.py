#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n and k is even.
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
        
    #State: `n` and `k` are integers read from the input, where `2 <= k <= n` and `k` is even; `permutation` is a list of `n` integers from 1 to `n` in a specific order determined by the loop; `idx` is 0; `idx_v` is 1; `curr_v` is `n + 1`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: result (where result is the space-separated string representation of the permutation list)
#Overall this is what the function does:The function reads two integers `n` and `k` from the input, where `2 <= k <= n` and `k` is even. It then constructs a permutation of `n` integers based on a specific pattern determined by `k` and prints the permutation as a space-separated string.

#State of the program right berfore the function call: This function does not have any parameters in its signature. It reads an integer t from the input, which represents the number of test cases. Each test case consists of two integers n and k, where n is the length of the desired permutation and k is the level of the permutation. It is guaranteed that k is even and 2 ≤ k ≤ n ≤ 2 · 10^5. The function then calls `func_1()` t times to process each test case.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, representing the number of test cases. For each test case, it processes the input values `n` and `k` by calling `func_1()`. After processing all test cases, it does not return any value.

