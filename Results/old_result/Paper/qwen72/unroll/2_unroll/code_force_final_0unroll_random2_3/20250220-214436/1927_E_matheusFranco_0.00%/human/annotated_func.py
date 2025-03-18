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
        
    #State: `n` and `k` remain unchanged, `permutation` is a list where the first `k` positions are filled with the integers from 1 to `k` in a pattern where each integer is placed at positions that are multiples of its index (0-based) plus the index itself, and the rest of the list remains zeros, `idx` is 0, `idx_v` is 1, `curr_v` is `k + 1`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: 1 2 3 2 1 3 1 2 3 2 (where the permutation list is filled with the integers from 1 to k in the specified pattern and the rest of the list remains zeros if n > k)
#Overall this is what the function does:The function `func_1` reads two integers, `n` and `k`, from the user input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It then generates a permutation list of length `n` where the first `k` positions are filled with integers from 1 to `k` in a pattern such that each integer `i` (1-based) is placed at positions that are multiples of `i-1` (0-based) plus `i-1`. The remaining positions in the list, if any, are filled with zeros. The function prints this permutation list as a space-separated string and does not return any value. The variables `n` and `k` remain unchanged after the function execution.

