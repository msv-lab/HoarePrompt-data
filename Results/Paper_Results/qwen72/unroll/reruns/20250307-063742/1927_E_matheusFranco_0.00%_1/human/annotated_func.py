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
        
    #State: `n` and `k` remain unchanged, `permutation` is a list of `n` integers where the first `k` values are filled with the sequence 1 to `k` in a pattern that repeats every `k` elements, `idx` is 0, `idx_v` is 1, `curr_v` is `k` + 1.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: "1 2 3 1 2 3 1 2 3 1" (where the string represents the space-separated values of the `permutation` list, and the pattern 1 to `k` repeats every `k` elements)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It generates a permutation list of length `n` where the first `k` values are filled with the sequence 1 to `k` in a repeating pattern. The final state of the program is that `n` and `k` remain unchanged, and the `permutation` list is printed as a space-separated string of integers. The function does not return any value.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. It repeatedly calls the function `func_1` a number of times specified by user input. After all calls to `func_1` are completed, the function terminates with the variable `t` set to 0.

