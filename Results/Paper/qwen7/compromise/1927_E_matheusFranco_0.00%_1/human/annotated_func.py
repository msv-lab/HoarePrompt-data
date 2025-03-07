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
        
    #State: Output State: After the loop executes all iterations, `multiples_of_k_plus_i` will be equal to `k * (n // k) * k`, which simplifies to `n * k`, since `n` is the total number of iterations and `k` is the step size. `permutation[multiples_of_k_plus_i]` will be `curr_v + (n // k)`, where `n // k` is the total number of iterations divided by `k`. The variable `i` will retain its initial value of `0`, and `curr_v` will be equal to `n`, the total number of iterations.
    #
    #In simpler terms, after the loop has completed all its iterations, `multiples_of_k_plus_i` will be equal to `n * k`, which is the product of the total number of iterations and the step size `k`. The value stored in the `permutation` list at the index `multiples_of_k_plus_i` will be `curr_v` plus the total number of iterations divided by `k`. The variable `i` will still be `0`, and `curr_v` will be equal to the total number of iterations `n`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: n + (n // k) [followed by the rest of the elements in the permutation list from index n * k to the end]
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from the standard input, where \( 2 \leq k \leq n \leq 2 \times 10^5 \) and \( k \) is even. It then constructs a list `permutation` of length \( n \) and fills it according to a specific pattern. Specifically, for each iteration from \( 0 \) to \( k-1 \), it places values starting from \( 1 \) up to \( n \) in the list at positions that are multiples of \( k \) plus the current iteration index. After completing these iterations, it prints the contents of the `permutation` list as a space-separated string. The function does not return any value.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: Output State: `t` is less than or equal to 0.
    #
    #This means that after all the iterations of the loop have finished, the value of `t` will be less than or equal to 0. This is because the loop decrements `t` by 1 in each iteration and continues as long as `t` is greater than 0. Once `t` becomes 0 or less, the condition `t > 0` in the loop head will no longer be true, and the loop will terminate.
#Overall this is what the function does:The function processes a specified number of test cases (`t`). For each test case, it reads two integers `n` and `k` (where `2 ≤ k ≤ n ≤ 2⋅10^5` and `k` is even), calls another function `func_1()` to perform some operations, and then decrements the counter `t`. After processing all test cases, it ensures that `t` is less than or equal to 0.

