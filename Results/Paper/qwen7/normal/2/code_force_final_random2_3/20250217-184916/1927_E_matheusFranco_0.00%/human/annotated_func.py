#State of the program right berfore the function call: n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5, k is even, and n - k + 1 ≥ 1.
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
        
    #State: Output State: `idx` is 1, `idx_v` is 1, `permutation` is a list of `n` elements where every `i * k`-th element (starting from `k`) is set to `i + 1` for all iterations `i` from 0 to `k-1`, `n` is an integer input from the user, `k` is an integer input from the user, `curr_v` is `n * k + 1`, `multiples_of_k_plus_i` is greater than or equal to `len(permutation)`.
    #
    #Explanation: After the loop completes all its iterations, the `permutation` list will have its elements set according to the rule specified in the loop body, with every `i * k`-th element (starting from `k`) being set to `i + 1`. The loop runs for `k` iterations, and during each iteration, `curr_v` is incremented by `k` each time `multiples_of_k_plus_i` is updated. Since the loop increments `curr_v` by 1 each time through the loop and there are `k` iterations, `curr_v` will be `k + 1` at the end of the first iteration, `2 * k + 1` at the end of the second iteration, and so on, up to `k * k + 1` at the end of the last iteration. Therefore, `curr_v` will be `n * k + 1` when the loop finishes. All other variables (`idx`, `idx_v`, `multiples_of_k_plus_i`) will be as described.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: "1 0 0 2 0 0 3 0 0 ..." (where the exact numbers depend on the values of n and k)
#Overall this is what the function does:The function reads two integers `n` and `k` from the user, where `2 ≤ k ≤ n ≤ 2⋅10^5`, `k` is even, and `n - k + 1 ≥ 1`. It then constructs a list `permutation` of length `n` and sets every `i * k`-th element (starting from index `k`) to `i + 1` for all iterations `i` from `0` to `k-1`. Finally, it prints the list `permutation` as a space-separated string.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: Output State: `t` is a non-positive integer.
    #
    #This means that after all the iterations of the loop have finished, the value of `t` will no longer be a positive integer. Since the loop decrements `t` by 1 in each iteration and stops when `t` is no longer greater than 0, `t` will eventually reach 0 or become negative, making it a non-positive integer.
#Overall this is what the function does:The function processes a specified number of test cases (determined by the initial value of `t`). For each test case, it reads two integers `n` and `k` (where `2 ≤ k ≤ n ≤ 2⋅10^5` and `k` is even), then calls another function `func_1()` to process these values. After processing all test cases, it outputs a non-positive integer (`t` becomes 0 or negative).

