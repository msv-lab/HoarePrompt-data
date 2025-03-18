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
        
    #State: idx is 1, n is an integer such that 2 ≤ n ≤ 2⋅10^5, k is an even integer such that 2 ≤ k ≤ n, and permutation is a list where each index that is a multiple of (i + k) for i in range(k) is filled with values from 1 to n in sequence, with the rest of the elements remaining as 0. curr_v is n + 1.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: - The `print(result)` statement will output the string representation of the `permutation` list.
    #
    #Given the initial state and the construction of the `permutation` list, the output will be a space-separated string of integers representing the `permutation` list.
    #
    #Output:
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from the standard input, where \( 2 \leq k \leq n \leq 2 \times 10^5 \) and \( k \) is even. It constructs a list `permutation` of length \( n \), filling specific indices based on the value of \( k \). Each index that is a multiple of \( (i + k) \) for \( i \) in the range of \( k \) is filled with consecutive integers starting from 1. All other indices remain 0. Finally, it prints the resulting list as a space-separated string. If the conditions on \( n \) and \( k \) are not met, the function will not execute correctly, leading to undefined behavior.

#State of the program right berfore the function call: t is a positive integer indicating the number of test cases, and for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads two integers `n` and `k` (where 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even), then calls another function `func_1()` to process these values. After processing all test cases, it sets `t` to 0.

