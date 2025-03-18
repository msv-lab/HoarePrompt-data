#State of the program right berfore the function call: n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5, k is even, and the values of n and k are provided as space-separated inputs on a single line for each test case.
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
        
    #State: Output State: `i` is 2, `k` is an even integer and `k` must be less than `n`, `permutation` is a list where the indices that are multiples of `k` are filled with consecutive integers starting from 2, `idx_v` is `len(permutation)`, `curr_v` is `len(permutation) + 2 * 3 * (k/2) + 1`, `multiples_of_k_plus_i` is `len(permutation)`, and `len(permutation)` is at least `k * (k/2) + 1`.
    #
    #**Explanation:**
    #- The loop iterates `k` times, and for each iteration `i`, it updates the `permutation` list at indices that are multiples of `k + i`.
    #- After `k` iterations, the loop will have filled all necessary indices in the `permutation` list that are multiples of `k`.
    #- The variable `i` will be `k - 1` after the last iteration, but since the loop uses `i` in the range `range(k)`, `i` will be `k - 1` just before the loop exits.
    #- `curr_v` starts at `len(permutation) + 1` and increments by 1 for each assignment made in the inner while loop. Since the loop runs `k` times and each time it makes `n // k` assignments (assuming `n` is large enough), `curr_v` will be `len(permutation) + k * (n // k)`.
    #- Given that `k` is even and the loop runs `k` times, the total number of assignments is `k * (n // k)`, leading to `curr_v` being `len(permutation) + 2 * 3 * (k/2) + 1` if we assume the worst-case scenario where `n` is just enough to fill all required indices.
    #- `multiples_of_k_plus_i` will be equal to `len(permutation)` because the loop exits when `multiples_of_k_plus_i` is no longer less than `len(permutation)`.
    #- `idx_v` remains `len(permutation)` because it is updated to the length of the `permutation` list after each assignment.
    #- `permutation` will have consecutive integers starting from 2 at all indices that are multiples of `k`, and the length of `permutation` will be at least `k * (k/2) + 1` to ensure all necessary indices are filled.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: 2 3 4
#Overall this is what the function does:The function processes two integers `n` and `k` as space-separated inputs, checks if `k` is even and within the range `2 ≤ k ≤ n ≤ 2⋅10^5`. If the conditions are met, it constructs a list `permutation` of length `n` and fills it with consecutive integers starting from 2 at indices that are multiples of `k`. Finally, it prints the contents of the `permutation` list as space-separated integers. If the conditions are not met, the function does not proceed further and no output is generated.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: Output State: `t` is equal to 0.
    #
    #Natural Language Explanation: After the loop has executed all its iterations, the value of `t` will be reduced by 1 for each iteration until it reaches 0. Since the loop continues as long as `t` is greater than 0, once `t` becomes 0, the loop terminates. Therefore, after all iterations, `t` will be equal to 0.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it reads two integers `n` and `k` such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even. For each test case, it calls `func_1()` which is not defined in the provided code. After processing all test cases, it ensures that the variable `t` is set to 0.

