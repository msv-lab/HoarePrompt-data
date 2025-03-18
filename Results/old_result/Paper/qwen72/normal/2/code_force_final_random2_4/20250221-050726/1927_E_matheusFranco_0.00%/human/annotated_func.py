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
        
    #State: After all iterations of the loop, `n` and `k` remain integers such that 2 <= k <= n <= 2 * 10^5 and k is even. The `permutation` list of length `n` is filled such that for each `i` from 0 to `k-1`, the elements at indices `i, i+k, i+2*k, ...` up to the last valid index are set to consecutive integers starting from `1`. The variable `curr_v` is now equal to `n + (n // k)`, which is the total number of elements filled in the `permutation` list. The variables `idx` and `idx_v` remain unchanged at 0 and 1, respectively.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: "1 5 2 6 3 7 4 8" (or the corresponding elements for the given `n` and `k`)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. It generates a permutation of integers from 1 to `n` such that for each `i` from 0 to `k-1`, the elements at indices `i, i+k, i+2*k, ...` up to the last valid index are set to consecutive integers starting from 1. The function then prints this permutation as a space-separated string. The variables `n` and `k` remain unchanged, and the function does not return any value.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
def func_2():
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: No variables are passed to the function `func_2`, `t` is now `0` (indicating the loop has completed its iterations), and `func_1()` has been called `t` times, where `t` is the initial value of `t`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. It reads an integer `t` from the user input, and then calls the function `func_1` exactly `t` times. After the function completes, `t` is reduced to `0`, indicating that the loop has finished executing. The function effectively repeats the execution of `func_1` based on the user-provided integer.

