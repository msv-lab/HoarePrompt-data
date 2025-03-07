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
        
    #State: `n` and `k` remain the same, `permutation` is a list of `n` integers where the first `k` indices are filled with the values from `1` to `k` in a pattern that repeats every `k` elements, `idx` is 0, `idx_v` is 1, `curr_v` is `k + 1`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: "1 2 3 ... 1 2 3" (where the pattern "1 2 3" repeats every `k` elements, and the total number of elements is `n`)
#Overall this is what the function does:The function `func_1` accepts no parameters but reads two integers `n` and `k` from user input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It generates a permutation list of length `n` where the values from `1` to `k` are repeated in a pattern every `k` elements. The function then prints this permutation list as a space-separated string. After the function concludes, `n` and `k` remain unchanged, and the permutation list is printed in the specified format.

