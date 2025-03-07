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
        
    #State: Output State: `idx` is 1, `n` is an integer input from the user, `k` is an integer input from the user, and both are such that 2 ≤ `k` ≤ `n` ≤ 2⋅10^5 and `k` is even; `permutation` is a list of length `n` where every `i` index that is a multiple of `k + j` for `j` in range(`k`) contains the value `j // (k // 2) + 1`, and `idx_v` is 1, `curr_v` is `k`. 
    #
    #In simpler terms, the `permutation` list will have its indices set to specific values based on the rules of the loop. For each `i` in the range of `k`, starting from `i`, every `k`-th index will be filled with a value that increments by 1 for each complete cycle through the range `k`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: a string of space-separated integers based on the `permutation` list, where each index that is a multiple of `k + j` for `j` in range(`k`) contains the value `j // (k // 2) + 1`
#Overall this is what the function does:The function reads two integers `n` and `k` from user input, where `2 ≤ k ≤ n ≤ 2⋅10^5` and `k` is even. It then constructs a list `permutation` of length `n` where certain indices are assigned specific values based on the rules defined within the loop. Finally, it prints a string of space-separated integers representing the `permutation` list.

