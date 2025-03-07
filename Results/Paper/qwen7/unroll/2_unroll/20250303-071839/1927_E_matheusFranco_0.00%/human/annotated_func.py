#State of the program right berfore the function call: n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
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
        
    #State: Output State: `idx` is 0, `idx_v` is 1, `n` is an integer where 2 ≤ `n` ≤ 2⋅10^5 and `k` is an integer where 2 ≤ `k` ≤ `n` and `k` is even, `permutation` is a list of length `n` where elements at positions 0, `k`, `2k`, ..., `k*(k-1)` are filled with values from 1 to `k`, and `curr_v` is `k+1`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: - The `print(result)` statement will print the string containing the numbers 1 through k separated by spaces.
    #
    #Therefore, the output will be a string with the numbers 1 through k separated by spaces.
    #
    #Output:
#Overall this is what the function does:The function reads two integers `n` and `k` from input, where `2 ≤ k ≤ n ≤ 2⋅10^5` and `k` is even. It then creates a list of length `n` called `permutation`. The function fills specific positions in this list with values from 1 to `k`, following a pattern based on `k`. Finally, it prints a string containing these values separated by spaces.

