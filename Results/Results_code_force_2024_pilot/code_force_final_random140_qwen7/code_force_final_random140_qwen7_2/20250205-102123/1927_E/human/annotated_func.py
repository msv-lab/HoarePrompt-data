#State of the program right berfore the function call: n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_1():
    n, k = map(int, input().split(' '))
    permutation = [0] * n
    bottom_v = 1
    top_v = n
    idx = 0
    while idx < k:
        multiples_of_k_plus_idx = idx
        
        while multiples_of_k_plus_idx < len(permutation):
            if idx % 2 == 0:
                permutation[multiples_of_k_plus_idx] = bottom_v
                bottom_v += 1
            else:
                permutation[multiples_of_k_plus_idx] = top_v
                top_v -= 1
            multiples_of_k_plus_idx += k
        
        idx += 1
        
    #State: The `permutation` list is completely filled with all integers from 1 to `n` exactly once, following a specific pattern determined by the loop's logic.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: "1 2 3 ... (n-1) n"
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from the standard input, where \( 2 \leq k \leq n \leq 2 \times 10^5 \) and \( k \) is even. It then constructs a permutation of integers from 1 to \( n \) following a specific pattern and prints the permutation as a space-separated string. The final state of the program is that the constructed permutation is printed to the standard output.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: Output State: `t` is equal to 0.
    #
    #Natural Language Description: After all the iterations of the loop have finished, the variable `t` will be equal to 0, as it is decremented by 1 in each iteration and starts from a positive integer value.
#Overall this is what the function does:The function processes a specified number of test cases (`t`). For each test case, it reads two integers `n` and `k` (where `2 ≤ k ≤ n ≤ 2⋅10^5` and `k` is even), calls another function `func_1()` to perform some operations, and then decrements `t` by 1. After processing all test cases, it ensures that `t` is equal to 0.

