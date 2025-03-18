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
        
    #State: Output State: `permutation` is a list where every element at index `i` (where `i` is a multiple of `k` plus `i` for each iteration of the outer loop) is set to the value of `curr_v` incremented from 1, and all other elements remain 0. `n` is the length of the permutation list, `k` is the integer obtained from the input split by space, `idx` is 0, `idx_v` is 1, `curr_v` is `k * (k + 1) // 2 + 1`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: 2 0 2 0 2 0
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from user input, where \( 2 \leq k \leq n \leq 2 \times 10^5 \) and \( k \) is even. It then constructs a list named `permutation` of length \( n \), setting specific indices to values based on a pattern involving \( k \). Finally, it prints the modified list as a space-separated string. If the input conditions are not met, the function does not return anything specific but ensures the input validation is performed.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads two integers `n` and `k` where `k` is even and within the range 2 ≤ k ≤ n ≤ 2⋅10^5. After processing all test cases, it sets `t` to 0. The function does not return any value.

