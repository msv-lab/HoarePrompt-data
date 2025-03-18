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
        
    #State: Output State: `idx` is 1, `n` is an integer input from the user, `k` is an integer input from the user, `permutation` is a list of length `n` where elements at positions `i`, `i+k`, `i+2*k`, ..., `i+(m-1)*k` (where `m` is the largest integer such that `i+(m-1)*k < n`) are set to values from `1` to `k` in ascending order, and the rest of the elements are `0`, `idx_v` is 1, `curr_v` is `k`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: - Since the `print` statement outputs the `result` string, the output will be the space-separated representation of the `permutation` list.
    #
    #Given the initial state and the construction of the `permutation` list, the output will be the string representation of the `permutation` list with elements separated by spaces.
    #
    #Output:
#Overall this is what the function does:The function reads two integers `n` and `k` from user input, ensuring that `2 ≤ k ≤ n ≤ 2⋅10^5`, `k` is even, and `n - k + 1 ≥ 1`. It then constructs a list `permutation` of length `n`, setting elements at positions `i`, `i+k`, `i+2*k`, ..., `i+(m-1)*k` (where `m` is the largest integer such that `i+(m-1)*k < n`) to values from `1` to `k` in ascending order, with the rest of the elements remaining `0`. Finally, it prints the space-separated string representation of the `permutation` list.

