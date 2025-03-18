#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n <= 2 * 10^5 and k is even.
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
        
    #State: `n` and `k` remain the same, `permutation` is a list of `n` elements where the elements at indices that are multiples of `k` plus `i` (for `i` in range `k`) are filled with consecutive integers starting from 1, `idx` is 0, `idx_v` is 1, `curr_v` is `k + 1`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: - The `print(result)` statement will print the string `result`, which contains the elements of the `permutation` list separated by spaces.
    #
    #Given the initial state and the construction of the `permutation` list, the output will be a string of the elements of `permutation` separated by spaces.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the user input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It then constructs a list `permutation` of length `n` where the elements at indices that are multiples of `k` plus `i` (for `i` in the range `0` to `k-1`) are filled with consecutive integers starting from 1. The function prints this list as a space-separated string and does not return any value. After the function concludes, `n` and `k` remain unchanged, and the list `permutation` contains the constructed sequence of integers.

#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads input from the user to determine the number of test cases and then calls `func_1()` for each test case.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: `t` is 0.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the user, representing the number of test cases. It then calls the function `func_1` `t` times. After all calls to `func_1` are completed, the function does not return any value, and the variable `t` is 0.

