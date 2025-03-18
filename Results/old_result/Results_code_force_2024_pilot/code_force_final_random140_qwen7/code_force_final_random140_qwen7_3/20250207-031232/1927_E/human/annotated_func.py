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
        
    #State: Output State: `idx` is either 3 or 4, `n` is an integer obtained from the input with \(2 \leq k \leq n \leq 2 \cdot 10^5\), `k` is an integer obtained from the input and it is even, `permutation` is a list of `n` integers where each element is either `bottom_v` or `top_v` based on the value of `idx` modulo 2, `bottom_v` is increased by 3 from its initial value, and `top_v` is decreased by 3 from its initial value, and `multiples_of_k_plus_idx` equals `n`.
    #
    #To understand this final state:
    #- The loop runs until `idx` reaches `k`. Since `k` is even and \(2 \leq k \leq n\), `idx` will eventually reach `k`.
    #- During each iteration, `multiples_of_k_plus_idx` is updated by adding `k` until it reaches or exceeds `n`.
    #- After all iterations, `idx` will be `k` (if `k` is less than or equal to 4, then `idx` will be `k` or `k+1`).
    #- `bottom_v` starts at 1 and increases by 1 for each valid index it fills, so after 3 iterations, it increases by 3.
    #- `top_v` starts at `n` and decreases by 1 for each valid index it fills, so after 3 iterations, it decreases by 3.
    #- Each valid index filled alternates between `bottom_v` and `top_v` based on whether `idx` is even or odd.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: result (where result is undefined)
#Overall this is what the function does:The function reads two integers \(n\) and \(k\) from input, where \(2 \leq k \leq n \leq 2 \cdot 10^5\) and \(k\) is even. It constructs a list `permutation` of length \(n\) where each element is either `bottom_v` or `top_v` based on the parity of the current index. Specifically, elements at indices that are multiples of \(k\) plus the current index are filled with `bottom_v` starting from 1 and increasing by 1 for each valid index, and elements at other indices are filled with `top_v` starting from \(n\) and decreasing by 1 for each valid index. After constructing the list, it prints the elements of the list as a space-separated string. If the conditions on \(n\) and \(k\) are not met, the function will raise an error.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: Output State: `t` is less than or equal to 0.
    #
    #Natural Language Description: After all the iterations of the loop have finished, the value of `t` will be less than or equal to 0, as the loop decrements `t` by 1 in each iteration until `t` is no longer greater than 0.
#Overall this is what the function does:The function processes up to `t` test cases, where for each test case, it accepts two integers `n` and `k` (with 2 ≤ k ≤ n ≤ 2⋅10^5 and k being even). It then calls another function `func_1()` for each test case without returning any specific value. After processing all test cases, it ensures that the variable `t` is less than or equal to 0.

