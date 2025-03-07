#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n <= 2 * 10^5 and k is even.
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
        
    #State: The `permutation` list is updated such that for each `i` in the range from 0 to `k-1`, the elements at indices `i, i+k, i+2k, ...` (up to the length of the `permutation` list) are filled with consecutive integers starting from `1`. The `curr_v` variable is updated to the next integer after the last value assigned in the `permutation` list. The variables `n`, `k`, `idx`, and `idx_v` remain unchanged.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: "elements of permutation separated by spaces" (where "elements of permutation" are the elements of the `permutation` list)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It then generates a permutation list of length `n` such that for each `i` in the range from 0 to `k-1`, the elements at indices `i, i+k, i+2k, ...` (up to the length of the list) are filled with consecutive integers starting from 1. The function prints the elements of this permutation list separated by spaces. After the function concludes, the variables `n` and `k` remain unchanged, and the permutation list is fully populated and printed.

