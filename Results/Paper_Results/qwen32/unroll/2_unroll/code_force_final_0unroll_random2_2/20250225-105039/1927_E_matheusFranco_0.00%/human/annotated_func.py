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
        
    #State: - The `permutation` list will have values filled in a pattern where each `i`th value of `curr_v` starts filling from the `i`-th position and fills every `k`-th position thereafter.
    #- `idx` remains 0 as it is not modified in the loop.
    #- `idx_v` remains 1 as it is not modified in the loop.
    #- `curr_v` will be `n + 1` after the loop as it is incremented `n` times.
    #
    #Output State:
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: result (where result is a space-separated string of values from the permutation list, constructed following the specific pattern defined by n and k)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `2 <= k <= n` and `k` is even. It constructs a permutation list of length `n` by filling it with values in a specific pattern: starting from each `i`-th position, it fills every `k`-th position thereafter with consecutive integers. Finally, it prints the permutation list as a space-separated string.

