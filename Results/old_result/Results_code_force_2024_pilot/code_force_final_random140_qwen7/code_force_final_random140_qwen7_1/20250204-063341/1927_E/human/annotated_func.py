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
        
    #State: The permutation list is fully filled according to the alternating pattern starting from 1 and going up to n.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: the permutation list elements separated by spaces (each element converted to a string)
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from input, where \( 2 \leq k \leq n \leq 2 \times 10^5 \) and \( k \) is even. It then constructs and prints a permutation of length \( n \) following an alternating pattern starting from 1 and ending at \( n \). If the conditions are not met, it does not return anything.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: Output State: `t` is equal to 0.
    #
    #Natural Language Description: After all the iterations of the loop have finished, the variable `t` will be equal to 0, as it is decremented by 1 in each iteration and starts from a positive integer (as implied by the given conditions).
#Overall this is what the function does:The function processes a specified number of test cases (`t`). For each test case, it reads two integers `n` and `k` where `2 ≤ k ≤ n ≤ 2⋅10^5` and `k` is even, then calls `func_1()` to perform some unspecified operation on these values. After processing all test cases, the variable `t` is set to 0.

