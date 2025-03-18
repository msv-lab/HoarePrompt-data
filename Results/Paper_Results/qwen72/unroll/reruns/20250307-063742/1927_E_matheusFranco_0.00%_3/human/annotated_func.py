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
        
    #State: `n` and `k` remain unchanged, `permutation` is a list of `n` elements where the first `k` elements are filled with the values from 1 to `k` in a pattern that repeats every `k` elements, `idx` is 0, `idx_v` is 1, `curr_v` is `k + 1`.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: "1 2 3 1 2 3 1 2" (where the elements of `permutation` are repeated in the pattern from 1 to `k` and the length of `permutation` is `n`)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from user input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It generates a list `permutation` of `n` elements, where the first `k` elements are filled with the values from 1 to `k` in a repeating pattern. The function then prints this list as a space-separated string. The function does not return any value, and the variables `n` and `k` remain unchanged after the function execution.

#State of the program right berfore the function call: None of the variables in the function signature are used, but the function assumes that `func_1` is defined and can handle the input and output for a single test case.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: `t` is 0.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, which represents the number of test cases. The function then calls `func_1` exactly `t` times. After all calls to `func_1` are completed, the function does not return any value, but the state of the program is such that `t` is 0.

