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
        
    #State: Output State: `idx` is 1, `n` is an integer input from the user, `k` is an integer input from the user, `permutation` is a list of length `n` where every element at index `i` (where `i % k == j` for `j` in range(k)) is set to `1 + (i // k) * (n // k)`, `idx_v` is 1, `curr_v` is `1 + (n * (n - 1)) // (2 * k)`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: "1 1 1 ... 1" (where the number 1 is repeated n//k times for each j in range(k))
#Overall this is what the function does:The function reads two integers `n` and `k` from the user, where `2 ≤ k ≤ n ≤ 2⋅10^5`, `k` is even, and `n - k + 1 ≥ 1`. It then constructs a list `permutation` of length `n` where each element at index `i` (such that `i % k == j` for `j` in range(`k`)) is set to `1 + (i // k) * (n // k)`. Finally, it prints the list as a space-separated string of integers.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads two integers `n` and `k` (where 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even), then calls another function `func_1()` which processes these values. After processing all test cases, the variable `t` is set to 0.

